
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import time

# убрала апи ключ
api = ''
bot = telebot.TeleBot(api)

url = "https://realestatemne24.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
house_cards = soup.find_all("div", class_="hp-grid__item hp-col-sm-4 hp-col-xs-12")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Recent Listings in Montengero'),types.KeyboardButton('Choose the certain city'))
    bot.send_message(message.chat.id, text= f'Hi, {message.from_user.first_name}. Lets find new apartment',reply_markup = keyboard)

@bot.message_handler(content_types=['text'])
def get_answer(message):
    if message.text == 'Recent Listings in Montengero':
        for item in house_cards[0:1]:
            item_header = item.find("h4", class_="hp-listing__title")
            item_link = item.find("div", class_="hp-listing__image")
            item_lin2 = item_link.find("a").get("href")
            item_en_name = item_header.find("a").text
            item_footer = item.find("footer", class_="hp-listing__footer")
            item_font = item_footer.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text
            ready_names = {
                'Name': item_en_name,
                'Price': item_font,
                'Link':item_lin2
            }

            # return f"{item_en_name}\n\n{item_font}\n\n{item_lin2}"
            time.sleep(0.25)
            bot.send_message(message.chat.id, {item_en_name})
            bot.send_message(message.chat.id, {item_lin2})
            bot.send_message(message.chat.id, {item_font},reply_markup =types.ReplyKeyboardRemove())
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keyboard.add(types.KeyboardButton('+'))
            bot.send_message(message.chat.id, text='*Show more recent apartments?*',
                             reply_markup=keyboard, parse_mode="Markdown")
    if message.text == '+':
        bot.send_message(message.chat.id, text="Let's visit our website :https://realestatemne24.com/",reply_markup =types.ReplyKeyboardRemove() )


    elif message.text == 'Choose the certain city':
        bot.send_message(message.chat.id,'Sending the link : https://realestatemne24.com/')






bot.polling(none_stop=True)

        