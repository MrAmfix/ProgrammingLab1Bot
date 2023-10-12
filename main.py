import telebot
from telebot import types
import random

bot = telebot.TeleBot("6374226963:AAHWJ8AgOnS8JIzvmDok4rX-QV1vhNIHGjQ")
user_states = {}

def is_correct_string(strx):
    strx = strx.lstrip()
    if strx[0] == "+" or strx[0] == "-":
        strx = strx[1:]
    strx += " "
    math_sign = ["+", "-", "*", "/"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arr_check = []
    curr_str = ""
    for i in strx:
        if i in math_sign or i == " ":
            if len(curr_str) != 0:
                if curr_str[-1] == ".":
                    return False
                else:
                    arr_check.append(curr_str)
                    curr_str = ""
            if i != " ":
                arr_check.append(i)
        elif i == ".":
            if len(curr_str) == 0:
                return False
            elif "." in curr_str:
                return False
            else:
                curr_str += i
        elif i in numbers:
            curr_str += i
        else:
            return False

    if (arr_check[0] in math_sign and (arr_check[0] != "-" or arr_check[0] != "+")) or (arr_check[-1] in math_sign):
        return False
    else:
        curr_state = ""
        if arr_check[0] in math_sign:
            curr_state = "SIGN"
        else:
            curr_state = "NUMBER"
        last_sign = ""
        for i in arr_check[1:]:
            if i in math_sign:
                if curr_state == "SIGN":
                    return False
                else:
                    last_sign = i
                    curr_state = "SIGN"
            else:
                if curr_state == "NUMBER":
                    return False
                else:
                    if last_sign == "/" and float(i) == 0:
                        return False
                    else:
                        curr_state = "NUMBER"
        return True

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
    test_lab2 = types.KeyboardButton("Проверить Lab#1")
    keyboard.add(link_reg, link_rep, test_lab2)
    return keyboard

def end_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Назад"))
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
    user = message.from_user
    fn = user.first_name
    ln = user.last_name if user.last_name else ""
    bot.send_message(message.from_user.id, f"Приветствую вас, {fn} {ln}, в Институте Теплых Мужских Отношений."
                                           f"\nМеня зовут It's Moshniy bot.\nЧем могу помочь?", reply_markup=start_keyboard())
    user_states[message.from_user.id] = "menu"

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == "menu")
def menu(message):
    if message.text == "Запись на сдачу":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=reg_keyboard())
        user_states[message.from_user.id] = "write"
    elif message.text == "Ссылки на учебные github":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=rep_keyboard())
        user_states[message.from_user.id] = "github"
    elif message.text == "Проверить Lab#1":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=end_keyboard())
        user_states[message.from_user.id] = "test"
    else:
        rand_message(message.text)
        bot.send_message(message.from_user.id, rand_message(message.text))

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == "test")
def test(message):
    if message.text == "Назад":
        bot.send_message(message.from_user.id, wait_message(), reply_markup=start_keyboard())
        user_states[message.from_user.id] = "menu"
    else:
        if is_correct_string(message.text):
            try:
                result = eval(message.text)
                bot.send_message(message.from_user.id, result)
            except Exception as e:
                bot.send_message(message.from_user.id, "Code Error!!!!")
        else:
            bot.send_message(message.from_user.id, "Неправильный формат строки")

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
