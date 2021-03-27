import re
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import link

from api import get_cards_info, Card

get_messages = re.compile("\#(\d+)").findall
bot = Bot(token=os.getenv("tg_trello_bot_bot_token"))
dp = Dispatcher(bot)


def nicer(card: Card):
    return link(card.name, card.link)


@dp.message_handler()
async def echo(message: types.Message):
    data = dict([x async for x in get_cards_info()])
    cards = [r for x in set(get_messages(message.text)) if (r := data.get(int(x)))]
    if len(cards) > 0:
        prep = "are" if len(cards) > 1 else "is"
        msg = ",\n".join(map(nicer, cards))
        await message.answer(f"{msg}\n{prep} mentioned", parse_mode=types.ParseMode.MARKDOWN)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
