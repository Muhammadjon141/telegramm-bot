
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Avto savdo"))

addresses_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
addresses_keyboard.add(KeyboardButton("1"))
addresses_keyboard.add(KeyboardButton("2"))
addresses_keyboard.add(KeyboardButton("Back"))
