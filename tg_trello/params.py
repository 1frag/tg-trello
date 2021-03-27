import aiohttp
import contextvars
import dotenv
import os

dotenv.load_dotenv("data.env")
V = contextvars.ContextVar

key: V[str] = V("key", default=os.getenv("tg_trello_bot_trello_key"))
token: V[str] = V("token", default=os.getenv("tg_trello_bot_trello_token"))
board_id: V[str] = V("board_id", default="")
session: V[aiohttp.ClientSession] = V("session")
