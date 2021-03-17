import asyncio
from aiogram import Bot, Dispatcher, executor
from config import bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=storage)


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp)
