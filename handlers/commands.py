import logging
import aiohttp

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

from config_reader import config

# router from commands
rc = Router()

logger = logging.getLogger(__name__)

API_KEY = config.API_KEY.get_secret_value()

@rc.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hi! I am a weather bot. Write /show_weather [city]')

async def get_weather(session, city):
    logger.info(f"get_weather: {city}")

    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        async with session.get(url) as response:
            
            logger.info(f"get_weather: {city} {response.status}")

            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']

                return (0, f"{temp}")

            else:
                return (1, "City is not found")

    except Exception as e:
        return (1, f"Data receiving error: {str(e)}")

async def main_get(city):
    async with aiohttp.ClientSession() as session:
        return await get_weather(session, city)


@rc.message(Command('show_weather'))
async def show_weather(message: types.Message):
    try: 
        city = message.text.split()[1]

        response = await main_get(city)

        error_check = response[0]

        if error_check == 0:
            temp = response[1]
            await message.answer(f'The weather in city {city} >> {temp}°C') 

    except IndexError:
        await message.answer('Please specify the city after the command!\n example: /show_weather Moscow')
    except Exception as e:
        await message.answer(f'Error: {str(e)}')

