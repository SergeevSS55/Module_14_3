from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ], resize_keyboard=True
)

ikb_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт 2', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт 3', callback_data="product_buying")],
        [InlineKeyboardButton(text='Продукт 4', callback_data="product_buying")],
    ], resize_keyboard=True
)
ikb_buy.row()
