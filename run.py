import asyncio
from aiogram import Bot, Dispatcher
import logging

from app.handlers import router


async def main():
    bot = Bot(token="your_telegram_token")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Error')
