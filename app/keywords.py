from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

# Главное меню (Reply клавиатура)
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Погода')],
        [KeyboardButton(text='О нас')]  # Каждая строка должна быть в отдельном списке
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

gorod = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Москва', callback_data='Moscow')],
        [InlineKeyboardButton(text='Челябинск', callback_data='Chelyabinsk')],
        [InlineKeyboardButton(text='Тюмень', callback_data='Tyumen')],
        [InlineKeyboardButton(text='Златоуст', callback_data='Zlatoust')],

        [InlineKeyboardButton(text='Кострома', callback_data='Kostroma')],
        [InlineKeyboardButton(text='Киров', callback_data='Kirov')],
        [InlineKeyboardButton(text='Калининград', callback_data='Kaliningrad')],
        [InlineKeyboardButton(text='Екатеринбург', callback_data='Ekaterinburg')],
        [InlineKeyboardButton(text='Кореновск', callback_data='Korenovsk')],
        [InlineKeyboardButton(text='Уфа', callback_data='Ufa')],
        [InlineKeyboardButton(text='Курган', callback_data='Kurgan')],
        [InlineKeyboardButton(text='Кемерово', callback_data='Kemerovo')],
        [InlineKeyboardButton(text='Казань', callback_data='Kazan')],
    ]
)

