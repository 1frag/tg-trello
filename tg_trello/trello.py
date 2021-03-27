from params import token, key, session, board_id

BASE_URL = "https://api.trello.com/1/"


async def get_boards():
    async with session.get().get(
            BASE_URL + "members/me/boards",
            params={
                "key": key.get(),
                "token": token.get(),
            }, headers={"content_type": "application/json"},
    ) as resp:
        return await resp.json()


async def get_cards():
    async with session.get().get(
            BASE_URL + f"boards/{board_id.get()}/cards",
            params={
                "key": key.get(),
                "token": token.get(),
            }, headers={"content_type": "application/json"},
    ) as resp:
        return await resp.json()
