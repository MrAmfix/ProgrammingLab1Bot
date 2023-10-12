import telebot
from telebot import types
import googlesearch
import random

bot = telebot.TeleBot("6374226963:AAHWJ8AgOnS8JIzvmDok4rX-QV1vhNIHGjQ")
user_states = {}



def wait_message():
    arr = ["💣", "🏀", "⚽", "🌚", "👨‍💻", "🤡", "💬"]
    return random.choice(arr)

def rand_message(text):
    return "Моя твоя не понимать"
    #return googlesearch.search(text)

def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    link_reg = types.KeyboardButton("Запись на сдачу")
    link_rep = types.KeyboardButton("Ссылки на учебные github")
    keyboard.add(link_reg, link_rep)
    return keyboard

def reg_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    inf = types.KeyboardButton("Информатика")
    prog = types.KeyboardButton("Программирование")
    alg = types.KeyboardButton("АиСД (Алгосы)")
    back = types.KeyboardButton("Назад")
    keyboard.add(inf, prog, alg, back)
    return keyboard

def rep_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    inf = types.KeyboardButton("Информатика")
    prog = types.KeyboardButton("Программирование")
    alg = types.KeyboardButton("АиСД (Алгосы)")
    infocom = types.KeyboardButton("ИнфоКом")
    back = types.KeyboardButton("Назад")
    keyboard.add(inf, prog, alg, infocom, back)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Приветствую вас, {message.from_user.username}, в Институте Теплых Мужских Отношений."
                                           f"\nМеня зовут It's Moshniy bot.\nЧем могу помочь?", reply_markup=start_keyboard())
    user_id = message.from_user.username
    if user_id == "Kabachok_1":
        bot.send_message(message.from_user.id, "А я знаю, что ты Леша")
    elif user_id == "muthafunk":
        bot.send_message(message.from_user.id, "А я знаю, что ты Артем")
    elif user_id == "n_e_q_u_m_a":
        bot.send_message(message.from_user.id, "А я знаю, что ты Егор Гагарин")
    user_states[message.from_user.id] = "menu"

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == "menu")
def menu(message):
    if message.text == "Запись на сдачу":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=reg_keyboard())
        user_states[message.from_user.id] = "write"
    elif message.text == "Ссылки на учебные github":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=rep_keyboard())
        user_states[message.from_user.id] = "github"
    else:
        rand_message(message.text)
        bot.send_message(message.from_user.id, rand_message(message.text))

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == "write")
def write(message):
    if message.text == "Информатика":
        bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/1JYlDSwy1Vq476NOECvPuv2WRePUNuDbUh0foLmCudKk/edit#gid=0")
    elif message.text == "Программирование":
        bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/15vU7odXOseENO622uKrtHb5fEtA1CyiPgBp7o71w6Jg/edit#gid=0")
    elif message.text == "АиСД (Алгосы)":
        bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/1KqvCFxAKWfi1XBONL9vUcadn424o-0GKa3ziSlR94hU/edit#gid=1064470743")
    elif message.text == "Назад":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=start_keyboard())
        user_states[message.from_user.id] = "menu"
    else:
        rand_message(message.text)
        bot.send_message(message.from_user.id, rand_message(message.text))

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == "github")
def github(message):
    canansw = ["Информатика", "Программирование", "АиСД (Алгосы)", "ИнфоКом"]
    if message.text == "Информатика":
        bot.send_message(message.from_user.id, "https://github.com/cs-itmo-2023")
    elif message.text == "Программирование":
        bot.send_message(message.from_user.id, "https://repeated-squid-629.notion.site/2023-2024-36763ed0edbf4cebbc722bdf21c94db6")
    elif message.text == "АиСД (Алгосы)":
        bot.send_message(message.from_user.id, "https://github.com/Algorithms-ICT-2023-2024")
    elif message.text == "ИнфоКом":
        bot.send_message(message.from_user.id, "https://drive.google.com/drive/folders/1TFb_bPQIp8WMBziS-4qtCNUXyylWLdMS")
    elif message.text == "Назад":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=start_keyboard())
        user_states[message.from_user.id] = "menu"
    else:
        rand_message(message.text)
        bot.send_message(message.from_user.id, rand_message(message.text))

bot.polling(none_stop=True, interval=0)
