import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import time
import googletrans
import os

# объект переводчика
translator = googletrans.Translator()

# элементы бота
api = ''
bot = telebot.TeleBot(api)

# парсер новинок

url_for_new = "https://realestatemne24.com/"
r = requests.get(url_for_new)
soup = BeautifulSoup(r.text, "lxml")
house_cards = soup.find_all("div", class_="hp-grid__item hp-col-sm-4 hp-col-xs-12")

# парсер домов
url_for_houses = "https://realestatemne24.com/?post_type=hp_listing&s=&_category=59"
r_for_uses = requests.get(url_for_houses)
soup_for_houses = BeautifulSoup(r_for_uses.text, "lxml")
houses_cards = soup_for_houses.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")

# парсер апартаментов
url_for_apartments = "https://realestatemne24.com/?post_type=hp_listing&s=&_category=58"
r_for_apartments = requests.get(url_for_apartments)
soup_for_apartments = BeautifulSoup(r_for_apartments.text, "lxml")
apartments_cards = soup_for_apartments.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Welcome to *ADRIATIC REAL ESTATE*, please choose the language\nДобро пожаловать в *ADRIATIC REAL ESTATE*, пожалуйста, выберите язык',parse_mode="Markdown")
    bot.send_message(message.chat.id, text='Наша команда состоит из опытных и знающих агентов по недвижимости,\nкоторые стремятся помочь нашим клиентам найти идеальную недвижимость.\nМы понимаем, что покупка или продажа недвижимости может быть сложной задачей,и поэтому мы стремимся сделать процесс максимально плавным и беззаботным.' ,parse_mode="Markdown")
    bot.send_message(message.chat.id, text='*Please wait*, beautiful video is downloading...',parse_mode="Markdown")
    # file = open("/Users/aleksandramirnova/Desktop/Immobilien bot/мелкий размер и скорость.mp4", "rb")
    # video_path = os.path.join(os.getcwd(), 'small7384.mp4')
    # bot.send_video(message.chat.id, video_path, "here it is!")
    bot.send_message(message.chat.id, text='*Please wait*, beautiful video is downloading...', parse_mode="Markdown")
    file = open("../imob/1234.mp4", "rb")
    bot.send_video(message.chat.id, file, "here it is!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('🇱🇷 US'),types.KeyboardButton('🇷🇺 RU'),types.KeyboardButton('🇷🇸 CR'))
    bot.send_message(message.chat.id, text= f'Hi, {message.from_user.first_name}',reply_markup = keyboard)


@bot.message_handler(content_types=['text'])
def get_answer(message):
# омериканцы
    if message.text == '🇱🇷 US':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Show Recent Listings in Montengero'),('Select a category (Houses/Apartments)'), types.KeyboardButton('Back to the languages'))
        bot.send_message(message.chat.id, text='Show Recent Listings in Montengero', reply_markup=keyboard)
    if message.text == 'Show Recent Listings in Montengero':
        for item in house_cards[0:5]:
            item_header = item.find("h4", class_="hp-listing__title")
            item_div_link = item.find("div", class_="hp-listing__image")
            item_link = item_div_link.find("a").get("href")
            item_en_name = item_header.find("a").text
            item_footer = item.find("footer", class_="hp-listing__footer")
            item_price = item_footer.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.25)
            bot.send_message(message.chat.id, {item_en_name})
            bot.send_message(message.chat.id, {item_link})
            bot.send_message(message.chat.id, {item_price})
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('+ yes'))
        bot.send_message(message.chat.id, text='*Show more recent apartments?*',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == '+ yes':
        bot.send_message(message.chat.id, text="Let's visit our website :https://realestatemne24.com/",reply_markup =types.ReplyKeyboardRemove() )
# выбор яхыка омериканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Back to the languages'), (types.KeyboardButton('Exit from the bot..')))
        bot.send_message(message.chat.id, text='Back to the languages', reply_markup=keyboard)
    if message.text == 'Exit from the bot..':
        bot.send_message(message.chat.id,
                     text="Goodbye!\nЕo get started type /start",
                     reply_markup=types.ReplyKeyboardRemove())

    if message.text == 'Back to the languages':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🇱🇷 US'), types.KeyboardButton('🇷🇺 RU'),
                     types.KeyboardButton('🇷🇸 CR'))
        bot.send_message(message.chat.id, text=f'Hi, {message.from_user.first_name}', reply_markup=keyboard)


    elif message.text=='Select a category (Houses/Apartments)':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Houses'), types.KeyboardButton('🏢 Apartments'))
        bot.send_message(message.chat.id, text=f'Searching for ...', reply_markup=keyboard)
# en_ver_houses
    if message.text == '🏠 Houses':
        bot.send_message(message.chat.id, text=f'Searching for houses...')
        for house in houses_cards[0:5]:
            house_header = house.find("div", class_="hp-listing__image")
            house_link = house_header.find("a").get("href")
            house_name = house_header.find("img").get("alt")
            house_location = house.find("div", class_="hp-listing__attribute hp-listing__attribute--location").text
            house_square = house.find("div", class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            house_price = house.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text
            # house_view = house.find("div", class_="hp-listing__attribute hp-listing__attribute--view").text

            time.sleep(0.5)
            bot.send_message(message.chat.id, {house_name})
            bot.send_message(message.chat.id, f'⛳️{house_location}')
            bot.send_message(message.chat.id, {house_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {house_link})
            bot.send_message(message.chat.id, f'💶{house_price}')
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('See more houses !!!'), types.KeyboardButton('🏢 Apartments'),
                     types.KeyboardButton('🏖 Land'), types.KeyboardButton('🏦 Commercial real estate'))
        bot.send_message(message.chat.id, text=f'☑️', reply_markup=keyboard)
    if message.text == "See more houses !!!":
        bot.send_message(message.chat.id, text="Let's visit our website :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",reply_markup=types.ReplyKeyboardRemove())
# выбор яхыка омериканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Back to the languages'), (types.KeyboardButton('Exit from the bot.')))
        bot.send_message(message.chat.id, text='Back to the languages', reply_markup=keyboard)
    if message.text == 'Exit from the bot.':
        bot.send_message(message.chat.id,
                     text="Goodbye!\nЕo get started type /start",
                     reply_markup=types.ReplyKeyboardRemove())
# en_ver_apartments
    if message.text == '🏢 Apartments':
        bot.send_message(message.chat.id, text=f'Searching for apartments...')
        for apartment in apartments_cards[0:5]:
            apartment_header = apartment.find("div", class_="hp-listing__image")
            apartment_link = apartment.find("a").get("href")
            apartment_name = apartment_header.find("img").get("alt")
            apartment_location = apartment.find("div",class_="hp-listing__attribute hp-listing__attribute--location").text
            apartment_square = apartment.find("div",class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            apartment_price = apartment.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.5)
            bot.send_message(message.chat.id, {apartment_name})
            bot.send_message(message.chat.id, f'⛳️{apartment_location}')
            bot.send_message(message.chat.id, {apartment_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {apartment_link})
            bot.send_message(message.chat.id, f'💶{apartment_price}')
            bot.send_message(message.chat.id, text='---------------------------------',
                             reply_markup=types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Houses'), types.KeyboardButton('See more apartments !!!'))
        bot.send_message(message.chat.id, text=f' ☑️', reply_markup=keyboard)


    if message.text == "See more apartments !!!":
        bot.send_message(message.chat.id,text="Let's visit our website :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",
                         reply_markup=types.ReplyKeyboardRemove())
# выбор яхыка омериканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Back to the languages'), (types.KeyboardButton('Exit from the bot')))
        bot.send_message(message.chat.id, text='Back to the languages', reply_markup=keyboard)
    if message.text == 'Exit from the bot':
        bot.send_message(message.chat.id,
                     text="Goodbye!\nЕo get started type /start",
                     reply_markup=types.ReplyKeyboardRemove())


# россияне
    elif message.text == '🇷🇺 RU':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Посмотреть последние объявления в Черногории'),('Выберите категорию (Дома/Апартаменты)'),types.KeyboardButton('К выбору языка'))
        bot.send_message(message.chat.id, text='Посмотреть последние объявления в Черногории', reply_markup=keyboard)

    elif message.text == 'Посмотреть последние объявления в Черногории':
        for item in house_cards[0:5]:
            item_header = item.find("h4", class_="hp-listing__title")
            item_div_link = item.find("div", class_="hp-listing__image")
            item_link = item_div_link.find("a").get("href")
            item_en_name = item_header.find("a").text
            item_ru_name = translator.translate(item_en_name, src='en',dest='ru').text
            item_footer = item.find("footer", class_="hp-listing__footer")
            item_price = item_footer.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.25)
            bot.send_message(message.chat.id, {item_en_name})
            bot.send_message(message.chat.id, {item_link})
            bot.send_message(message.chat.id, {item_price})
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('+'))
        bot.send_message(message.chat.id, text='*Посмотреть больше новых объявлений?*',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == '+':
        bot.send_message(message.chat.id, text="Посетите наш сайт :https://realestatemne24.com/",reply_markup =types.ReplyKeyboardRemove())

# выбор языка в конце
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('К выбору языка'),types.KeyboardButton('Выйти из бота...'))
        bot.send_message(message.chat.id, text='Выберите язык:',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == 'Выйти из бота...':
        bot.send_message(message.chat.id,
                     text="До свидания!\nДля запуска напишите /start",
                     reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'К выбору языка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🇱🇷 US'), types.KeyboardButton('🇷🇺 RU'),
                     types.KeyboardButton('🇷🇸 CR'))
        bot.send_message(message.chat.id, text=f'Здравствуйте, {message.from_user.first_name}', reply_markup=keyboard)

    elif message.text=='Выберите категорию (Дома/Апартаменты)':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Дома'), types.KeyboardButton('🏢 Апартаменты'))
        bot.send_message(message.chat.id, text=f'Ищем подходящие варианты ...', reply_markup=keyboard)
# дома россияне
    if message.text == '🏠 Дома':
        bot.send_message(message.chat.id, text=f'Ищем дома...')
        for house in houses_cards[0:5]:
            house_header = house.find("div", class_="hp-listing__image")
            house_link = house_header.find("a").get("href")
            house_en_name = house_header.find("img").get("alt")
            house_ru_name = translator.translate(house_en_name, src='en',dest='ru').text
            house_location = house.find("div", class_="hp-listing__attribute hp-listing__attribute--location").text
            house_ru_location = translator.translate(house_location, src='en',dest='ru').text
            house_square = house.find("div", class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            house_price = house.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text
            # house_view = house.find("div", class_="hp-listing__attribute hp-listing__attribute--view").text

            time.sleep(0.5)
            bot.send_message(message.chat.id, {house_ru_name})
            bot.send_message(message.chat.id, f'⛳️{house_ru_location}')
            bot.send_message(message.chat.id, {house_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {house_link})
            bot.send_message(message.chat.id, f'💶{house_price}')
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Посмотреть больше домов!'), types.KeyboardButton('🏢 Апартаменты'))
        bot.send_message(message.chat.id, text=f' ...', reply_markup=keyboard)
    if message.text == 'Посмотреть больше домов!':
        bot.send_message(message.chat.id, text=" ☑️  Посетите наш сайт :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",reply_markup=types.ReplyKeyboardRemove())
# выбор языка в конце
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('К выбору языка'),types.KeyboardButton('Выйти из бота.'))
        bot.send_message(message.chat.id, text='Выберите язык:',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == 'Выйти из бота.':
        bot.send_message(message.chat.id,
                     text="До свидания!\nДля запуска напишите /start",
                     reply_markup=types.ReplyKeyboardRemove())
# апартаменты россияне
    if message.text == '🏢 Апартаменты':
        bot.send_message(message.chat.id, text=f'Ищем апартаменты...')
        for apartment in apartments_cards[0:5]:
            apartment_header = apartment.find("div", class_="hp-listing__image")
            apartment_link = apartment.find("a").get("href")
            apartment_name = apartment.find("img").get("alt")
            apartament_name_ru =translator.translate(apartment_name, src='en',dest='ru').text
            apartment_location = apartment.find("div",class_="hp-listing__attribute hp-listing__attribute--location").text
            apartament_location_ru = translator.translate(apartment_location, src='en',dest='ru').text
            apartment_square = apartment.find("div",class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            apartment_price = apartment.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.5)
            bot.send_message(message.chat.id, {apartament_name_ru})
            bot.send_message(message.chat.id, f'⛳️{apartament_location_ru}')
            bot.send_message(message.chat.id, {apartment_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {apartment_link})
            bot.send_message(message.chat.id, f'💶{apartment_price}')
            bot.send_message(message.chat.id, text='---------------------------------',
                             reply_markup=types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Дома'), types.KeyboardButton('Посмотреть больше апартаментов !!!'))
        bot.send_message(message.chat.id, text=f'☑️', reply_markup=keyboard)


    if message.text == 'Посмотреть больше апартаментов !!!':
        bot.send_message(message.chat.id,text="Посетите наш сайт :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",
                         reply_markup=types.ReplyKeyboardRemove())
# выбор языка в конце
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('К выбору языка'),types.KeyboardButton('Выйти из бота..'))
        bot.send_message(message.chat.id, text='Выберите язык:',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == 'Выйти из бота..':
        bot.send_message(message.chat.id,
                     text="До свидания!\nДля запуска напишите /start",
                     reply_markup=types.ReplyKeyboardRemove())
# балканцы
    elif message.text == '🇷🇸 CR':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Погледајте недавни огласи у Монтенегру'),('Изаберите категорију  (Куће/Апартмани)'),types.KeyboardButton('Избор језика'))
        bot.send_message(message.chat.id, text='Погледајте недавни огласи у Монтенегру', reply_markup=keyboard)
    elif message.text == 'Погледајте недавни огласи у Монтенегру':
        for item in house_cards[0:5]:
            item_header = item.find("h4", class_="hp-listing__title")
            item_div_link = item.find("div", class_="hp-listing__image")
            item_link = item_div_link.find("a").get("href")
            item_en_name = item_header.find("a").text
            item_sr_name = translator.translate(item_en_name, src='en',dest='sr').text
            item_footer = item.find("footer", class_="hp-listing__footer")
            item_price = item_footer.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.25)
            bot.send_message(message.chat.id, {item_sr_name})
            bot.send_message(message.chat.id, {item_link})
            bot.send_message(message.chat.id, {item_price})
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('+ добро'))
        bot.send_message(message.chat.id, text='*Прикажи новије станове?*',
                         reply_markup=keyboard, parse_mode="Markdown")
    if message.text == '+ добро':
        bot.send_message(message.chat.id, text="Посетимо нашу веб страницу :https://realestatemne24.com/",reply_markup =types.ReplyKeyboardRemove())
# выбор яхыка балканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Избор језика'), (types.KeyboardButton('Изађите из бота...')))
        bot.send_message(message.chat.id, text='Избор језика', reply_markup=keyboard)
    if message.text == 'Изађите из бота...':
        bot.send_message(message.chat.id,
                     text="Збогом!\nЗа покретање напишите /start",
                     reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Избор језика':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🇱🇷 US'), types.KeyboardButton('🇷🇺 RU'),
                     types.KeyboardButton('🇷🇸 CR'))
        bot.send_message(message.chat.id, text=f'Здраво, {message.from_user.first_name}', reply_markup=keyboard)

    elif message.text=='Изаберите категорију  (Куће/Апартмани)':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Куће'), types.KeyboardButton('🏢 Апартмани'))
        bot.send_message(message.chat.id, text=f'Тражите одговарајуће опције ...', reply_markup=keyboard)
# дома балканцы
    if message.text == '🏠 Куће':
        bot.send_message(message.chat.id, text=f'Тражите куће...')
        for house in houses_cards[0:5]:
            house_header = house.find("div", class_="hp-listing__image")
            house_link = house_header.find("a").get("href")
            house_en_name = house_header.find("img").get("alt")
            house_sr_name = translator.translate(house_en_name, src='en',dest='sr').text
            house_location = house.find("div", class_="hp-listing__attribute hp-listing__attribute--location").text
            house_sr_location = translator.translate(house_location, src='en',dest='sr').text
            house_square = house.find("div", class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            house_price = house.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text
            # house_view = house.find("div", class_="hp-listing__attribute hp-listing__attribute--view").text

            time.sleep(0.1)
            bot.send_message(message.chat.id, {house_sr_name})
            bot.send_message(message.chat.id, f'⛳️{house_sr_location}')
            bot.send_message(message.chat.id, {house_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {house_link})
            bot.send_message(message.chat.id, f'💶{house_price}')
            bot.send_message(message.chat.id, text='---------------------------------',reply_markup =types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Погледајте још кућа!'), types.KeyboardButton('🏢 Апартмани'))
        bot.send_message(message.chat.id, text=f'☑️', reply_markup=keyboard)
    if message.text == 'Погледајте још кућа!':
        bot.send_message(message.chat.id, text=" Посетите наш сајт :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",reply_markup=types.ReplyKeyboardRemove())
# выбор яхыка балканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Избор језика'), (types.KeyboardButton('Изађите из бота.')))
        bot.send_message(message.chat.id, text='Избор језика', reply_markup=keyboard)
    if message.text == 'Изађите из бота.':
        bot.send_message(message.chat.id,
                     text="Збогом!\nЗа покретање напишите /start",
                     reply_markup=types.ReplyKeyboardRemove())

 # сербские аппартаменты
    if message.text == '🏢 Апартмани':
        bot.send_message(message.chat.id, text=f'Тражите апартмане...')
        for apartment in apartments_cards[0:5]:
            apartment_header = apartment.find("div", class_="hp-listing__image")
            apartment_link = apartment.find("a").get("href")
            apartment_name = apartment.find("img").get("alt")
            apartament_name_sr = translator.translate(apartment_name, src='en',dest='sr').text
            apartment_location = apartment.find("div", class_="hp-listing__attribute hp-listing__attribute--location").text
            apartament_location_sr = translator.translate(apartment_location, src='en',dest='sr').text
            apartment_square = apartment.find("div",class_="hp-listing__attribute hp-listing__attribute--square-meter").text
            apartment_price = apartment.find("div", class_="hp-listing__attribute hp-listing__attribute--price").text

            time.sleep(0.5)
            bot.send_message(message.chat.id, {apartament_name_sr})
            bot.send_message(message.chat.id, f'⛳️{apartament_location_sr}')
            bot.send_message(message.chat.id, {apartment_square})
            # bot.send_message(message.chat.id, {house_view})
            bot.send_message(message.chat.id, {apartment_link})
            bot.send_message(message.chat.id, f'💶{apartment_price}')
            bot.send_message(message.chat.id, text='---------------------------------',
                             reply_markup=types.ReplyKeyboardRemove())

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('🏠 Куће'), types.KeyboardButton('Погледајте још кућа!!!'))
        bot.send_message(message.chat.id, text=f'☑️', reply_markup=keyboard)

    if message.text == 'Погледајте још кућа!!!':
        bot.send_message(message.chat.id,text="☑️  Посетите наш сајт :https://realestatemne24.com/?post_type=hp_listing&s=&_category=58",
                     reply_markup=types.ReplyKeyboardRemove())
# выбор яхыка балканцы
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.add(types.KeyboardButton('Избор језика'),(types.KeyboardButton('Изађите из бота..')))
        bot.send_message(message.chat.id, text='Избор језика',reply_markup=keyboard)
    if message.text == 'Изађите из бота..':
        bot.send_message(message.chat.id,
                         text="Збогом!\nЗа покретање напишите /start",
                             reply_markup=types.ReplyKeyboardRemove())

bot.polling(none_stop=True)
