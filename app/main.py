import asyncio
from aiogram import Router, Dispatcher, Bot, types, F
import os
import sqlite3
from handlers import user_commands
from dotenv import load_dotenv
from callback import query


async def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    bot = Bot(token=token)
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(user_commands.router,query.router)
    await dp.start_polling(bot)
        
if __name__ == "__main__":
    asyncio.run(main())