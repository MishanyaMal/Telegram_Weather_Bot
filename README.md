# Weather Telegram Bot

A simple Telegram bot that provides current weather information for any city. Users send a city name, and the bot returns temperature, humidity, wind speed, and weather conditions.

## Features

- **City‑Based Weather:** Get weather data by sending a city name (e.g., `London`, `Tokyo`).
- **Real‑Time Data:** Fetches the latest weather from OpenWeatherMap API.
- **User‑Friendly Output:** Displays weather in a clean, readable format in the chat.
- **Error Handling:** Gracefully handles invalid city names or API errors.
- **Easy Configuration:** All settings are in a single config file.

## Technologies Used

- **Language:** `Python`
- **Telegram Bot Framework:** `aiogram` (modern asynchronous framework for Telegram bots)
- **HTTP Client:** `aiohttp` library
- **Weather Data Provider:** OpenWeatherMap (https://openweathermap.org/api)

### Prerequisites

- Python 3.8 or higher
- A Telegram account
- An OpenWeatherMap account (https://openweathermap.org/api)
- API keys for both Telegram and OpenWeatherMap

### Step‑by‑Step Guide

1. **Create a Telegram Bot:**
   - Message `@BotFather` on Telegram.
   - Use the `/newbot` command to create a new bot.
   - Copy the **API Token** provided by BotFather.

2. **Get Your OpenWeatherMap API Key:**
   - Sign up at https://openweathermap.org/api.
   - Go to your account dashboard and generate a new **API Key**.
   - Keep it secure — do not share it publicly.
