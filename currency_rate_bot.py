import telebot
import requests
from requests import RequestException


TELE_TOKEN = 'your_telegram_bot_token'  # Telegram bot token
CURRENCY_URL = 'https://api.currencyapi.com/v3/latest'  # API URL for currency rates
API_KEY = 'your_currencyapi_key'  # API key for currency service
CURRENCY = 'RUB'  # Default currency is set to Russian Rubles
BASE_CURRENCY = 'USD'  # Base currency is set to US Dollar


# Function to retrieve currency rate from API
def get_currency(base_currency, currency, apikey, currency_url):
    params = dict(
        base_currency=base_currency,
        currencies=currency,
        apikey=apikey
    )
    rate = None

    try:
        # Send a request to the currency API to get the current USD to RUB exchange rate
        resp = requests.get(currency_url, params=params)
        if resp.status_code == 200:
            # If the request is successful, parse the JSON response
            resp_data = resp.json()
            # Get the exchange rate value for RUB
            rate = resp_data.get('data', {}).get(currency, {}).get('value')

    except (RequestException, ValueError, KeyError):
        pass  # Ignore errors and just return None if something goes wrong

    return rate


cache = {}  # Dictionary to store usernames

bot = telebot.TeleBot(TELE_TOKEN)  # Initialize the bot with the provided token


# Handler for the '/restart' and '/start' commands
@bot.message_handler(commands=['restart', 'start'])
def send_welcome(message):
    # Send a greeting message asking for the user's name
    bot.send_message(message.from_user.id, "Добрый день. Как вас зовут?")
    # Remove the user's name from cache (if exists) to request it again
    cache.pop(message.from_user.id, None)


# Handler for processing text messages
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Check if the user's name is already stored in the cache
    name = cache.get(message.from_user.id)
    if name:
        welcome = f'{name}!'
    else:
        # If the name is not stored, save it to the cache and greet the user
        name = message.text.title()
        welcome = f'Рад знакомству, {name}!'
        cache[message.from_user.id] = name

    rate_mes = 'не удалось выяснить.'  # Default message for failed currency retrieval

    rate = get_currency(BASE_CURRENCY, CURRENCY, API_KEY, CURRENCY_URL)

    if rate:
        rate_mes = f'{rate:.2f} руб.'  # Format the rate message

    # Construct the reply message with the user's name and exchange rate
    reply_mes = f'{welcome} Курс доллара сегодня {rate_mes}'
    bot.send_message(message.from_user.id, reply_mes)  # Send the message to the user


# -------------------------------------------------
if __name__ == '__main__':
    bot.infinity_polling()  # Keep the bot running to handle messages continuously
