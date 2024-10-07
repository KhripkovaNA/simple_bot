# Telegram Currency Bot

This Telegram bot provides the current exchange rate of USD to RUB (Russian Ruble) and interacts with users in a personalized way. It uses the [TeleBot](https://pypi.org/project/pyTelegramBotAPI/) library for handling Telegram API interactions and the [CurrencyAPI](https://currencyapi.com/) to fetch real-time exchange rate data.

## Features
- **Welcome Message**: The bot greets users when they send `/start` or `/restart` commands and asks for their name.
- **Personalized Responses**: The bot stores the user's name and uses it in future responses.
- **Real-time Currency Rate**: The bot retrieves the latest USD to RUB exchange rate using the CurrencyAPI.
- **Caching**: Usernames are cached to avoid asking the user's name repeatedly in the same session.

## How It Works
1. When the bot receives the `/start` or `/restart` command, it asks for the user's name.
2. The user enters their name in response.
3. The bot retrieves the latest USD to RUB exchange rate from the CurrencyAPI.
4. The bot replies with a personalized greeting and provides the exchange rate.
5. If the bot cannot retrieve the exchange rate, it notifies the user that the rate could not be retrieved.

## Installation

To run this bot locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/KhripkovaNA/telegram-currency-bot.git
   cd telegram-currency-bot
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your **Telegram Bot Token** and **CurrencyAPI Key** in the Python script:
   ```bash
   TELE_TOKEN = 'your_telegram_bot_token'
   API_KEY = 'your_currencyapi_key'
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

- **Commands**:
  - `/start`: Starts the bot and asks for the user's name.
  - `/restart`: Resets the session and asks for the user's name again.
- **Interactive Messages**:
  - The bot replies with a personalized greeting and provides the current USD to RUB exchange rate.

## Technologies Used

- **Python**: The programming language used for building the bot.
- **TeleBot (pyTelegramBotAPI)**: A Python wrapper for Telegram's Bot API.
- **requests**: A library for sending HTTP requests to the CurrencyAPI.
- **CurrencyAPI**: A real-time API for fetching currency exchange rates.
