import asyncio
from aiogram import Bot, Dispatcher

from app.henders import router


async def main():
    bot = Bot(token='7806678978:AAHhQ0o5wqqi9rf07jrVsk5ofe5u0wYwyWM')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")

