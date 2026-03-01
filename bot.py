import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import commands

bot = Bot(
	token=config.BOT_TOKEN.get_secret_value()
)

dp = Dispatcher()

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Диспетчер
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_routers(
        commands.rc
    )

    await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())
