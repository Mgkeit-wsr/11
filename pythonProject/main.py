import time
import traceback
import telebot
import tok
from telebot import types

bot = telebot.TeleBot(tok.TOKEN3)

@bot.message_handler(commands=['start'])
def start(message):
    namepo = f'Здраствуйте , <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Институт')
    website2 = types.KeyboardButton('Колледж')
    markup2.add(website, website2)
    bot.send_message(message.chat.id, namepo, parse_mode='html', reply_markup=markup2)

@bot.message_handler(content_types=['text'])
def get_text(message):
    mgy = open('mgy.jpg', 'rb')
    mfti = open('mifi.jpg', 'rb')
    mifi = open('mfti.jpg', 'rb')

    kol1 = open('kool1.jpg', 'rb')
    kol2 = open('koll2.jpg', 'rb')
    kol3 = open('koll3.jpg', 'rb')
    if message.text.lower() == 'институт':
        bot.send_message(message.chat.id, 'Топ три института Москвы', parse_mode='html')
        bot.send_photo(message.chat.id, mgy, parse_mode='html')
        bot.send_message(message.chat.id, 'Московский государственный университет имени М.В. Ломоносова\nАдрес: ул. Ленинские Горы, 1, Москва\nEmail: info@rector.msu.ru')
        bot.send_photo(message.chat.id, mfti, parse_mode='html')
        bot.send_message(message.chat.id, 'Московский физико-технический институт (Государственный университет)\nАдрес: г. Долгопрудный (Московская обл.), Институтский пер., д. 9\nEmail: pk@mipt.ru')
        bot.send_photo(message.chat.id, mifi, parse_mode='html')
        bot.send_message(message.chat.id, 'Национальный исследовательский ядерный университет «МИФИ»\nАдрес: г. Москва, Мясницкая ул., д. 20\nEmail: rector@mephi.ru')
    elif message.text.lower() == 'колледж':
        bot.send_message(message.chat.id, 'Топ три колледжа Москвы', parse_mode='html')
        bot.send_photo(message.chat.id, kol1, parse_mode='html')
        bot.send_message(message.chat.id, 'Колледж Архитектуры, Дизайна и Реинжиниринга № 26\nАдрес: г. Москва, ул. 5-я Кожуховская, д. 26, каб. 104\nEmail: priem@26kadr.ru')
        bot.send_photo(message.chat.id, kol2, parse_mode='html')
        bot.send_message(message.chat.id, 'Технологический колледж № 34\nАдрес: г. Москва, ул. Нагатинская, д. 4, корп. 1\nEmail: spo-34@edu.mos.ru')
        bot.send_photo(message.chat.id, kol3, parse_mode='html')
        bot.send_message(message.chat.id, 'Московский городской открытый колледж\nАдрес:  г. Москва, Волгоградский пр-т., д. 32, корп. 5, каб. 100\nEmail: info@open-college.ru')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except telebot.apihelper:
        print(traceback.format_exc())
        time.sleep(3)