import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import aiohttp

API_KEY = 'c6fb0d6fb2d26c84aaa9feaa5c703e8e'
BOT_TOKEN = '8146333746:AAFw-Jj-BghNwORJ5PUQg8bPFEwMtcDoTGg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
	await message.answer('Привет! Я бот погоды. Напиши /show_weather [город]')


async def get_weather(session, city):
	try:
		url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

		async with session.get(url) as response:
			if response.status == 200:
				data = await response.json()
				temp = data['main']['temp']

				return (0, f"{temp}")

			else:
				return (1, "Город не найден")

	except Exception as e:
		return (1, f"Ошибка при получении данных: {str(e)}")

async def main_get(city):
	async with aiohttp.ClientSession() as session:
		return await get_weather(session, city)


@dp.message(Command('show_weather'))
async def show_weather(message: types.Message):
	try: 
		city = message.text.split()[1]

		response = await main_get(city)

		error_check = response[0]

		if error_check == 0:
			temp = response[1]
			await message.answer(f'Погода в городе {city} >> {temp}°C')	

	except IndexError:
		await message.answer('Пожалуйста, укажите город после команды!\nПример: /show_weather Москва')
	except Exception as e:
		await message.answer(f'Произошла ошибка: {str(e)}')

async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())