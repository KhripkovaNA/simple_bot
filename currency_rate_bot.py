import telebot
import requests


TELE_TOKEN = '7700153592:AAHlWJZQOPAFPlI5PbfPQ6Qiowk7O_aqYEg'  # Telegram bot token
CURRENCY_URL = 'https://api.currencyapi.com/v3/latest'  # API URL for currency rates
API_KEY = 'cur_live_QWTlbZ4CXH5ZUOGH63JHJJxp4evUBKcsW9zXvyDO'  # API key for currency service

cache = {}  # Dictionary to store user names

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
    currency = 'RUB'  # Default currency is set to Russian Rubles
    rate_mes = 'не удалось выяснить.'  # Default message for failed currency retrieval
    params = dict(
        base_currency='USD',  # Base currency is set to US Dollar
        currencies=currency,
        apikey=API_KEY
    )
    try:
        # Send a request to the currency API to get the current USD to RUB exchange rate
        resp = requests.get(CURRENCY_URL, params=params)
        if resp.status_code == 200:
            # If the request is successful, parse the JSON response
            resp_data = resp.json()
            # Get the exchange rate value for RUB
            rate = resp_data.get('data', {}).get(currency, {}).get('value')
            if rate:
                rate_mes = f'{rate:.2f} руб.'  # Format the rate message
    except:
        pass  # Ignore any errors during the request

    # Check if the user's name is already stored in the cache
    name = cache.get(message.from_user.id)
    if name:
        welcome = f'{name}!'
    else:
        # If the name is not stored, save it to the cache and greet the user
        name = message.text.title()
        welcome = f'Рад знакомству, {name}!'
        cache[message.from_user.id] = name

    # Construct the reply message with the user's name and exchange rate
    reply_mes = f'{welcome} Курс доллара сегодня {rate_mes}'
    bot.send_message(message.from_user.id, reply_mes)  # Send the message to the user


# -------------------------------------------------
if __name__ == '__main__':
    bot.infinity_polling()  # Keep the bot running to handle messages continuously

