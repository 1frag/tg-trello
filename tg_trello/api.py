import asyncio
import aiohttp
import pydantic

import trello
import params


class Card(pydantic.BaseModel):
    id: int
    name: str
    link: str


def set_key():
    if not params.key.get():
        params.key.set(input("key: "))


def set_token():
    if not params.token.get():
        params.token.set(input("token: "))


async def get_cards_info():
    set_key()
    set_token()

    async with aiohttp.ClientSession() as session:
        params.session.set(session)

        if not params.board_id.get():
            for board in await trello.get_boards():
                if board["name"] == "Процессы разработки":
                    params.board_id.set(board["id"])

        for card in await trello.get_cards():
            yield card["idShort"], Card(
                id=card["idShort"],
                name=card["name"],
                link="https://trello.com/c/" + card["shortLink"],
            )


if __name__ == "__main__":
    async def test():
        import json
        print(json.dumps(dict([x async for x in get_cards_info()])))

    asyncio.run(test())
