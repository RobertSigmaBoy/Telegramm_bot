from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)
from states import RATE

async def my_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("статистика knb", callback_data="knb_state")],
        [InlineKeyboardButton("статистика knz", callback_data="knz_state")],
        [InlineKeyboardButton("статистика bac", callback_data="bac_state")],
        [InlineKeyboardButton("Назад", callback_data="back")],
    ]

    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Ваша статистика:", reply_markup=markup)
    return RATE

async def knb_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("статистика knb", callback_data="knb_state")],
        [InlineKeyboardButton("статистика knz", callback_data="knz_state")],
        [InlineKeyboardButton("статистика bac", callback_data="bac_state")],
        [InlineKeyboardButton("Назад", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    # Вызвать фунцию \n
    # 1. alex123 - 70
    # 2. anton32 - 20
    await query.edit_message_text("Статистика КНБ", reply_markup=markup)
    return RATE

async def knz_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("статистика knb", callback_data="knb_state")],
        [InlineKeyboardButton("статистика knz", callback_data="knz_state")],
        [InlineKeyboardButton("статистика bac", callback_data="bac_state")],
        [InlineKeyboardButton("Назад", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("статистика КНZ", reply_markup=markup)
    return RATE

async def bac_stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("статистика knb", callback_data="knb_state")],
        [InlineKeyboardButton("статистика knz", callback_data="knz_state")],
        [InlineKeyboardButton("статистика bac", callback_data="bac_state")],
        [InlineKeyboardButton("Назад", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("статистика bac", reply_markup=markup)
    return RATE
