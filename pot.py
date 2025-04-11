import telebot 
from config import *
API_TOKEN = TOKEN
from main import *
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def handler_message(message):
    prompt = message.text


    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API, KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]
    file_path = 'decoded_image.jpg'
    api.save_image(images,file_path)
    with open(file_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)




bot.infinity_polling()

