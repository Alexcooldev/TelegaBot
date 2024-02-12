from aiogram import Bot
from aiogram.types import Message
from keybords.registr_kb import register_keyboard
from keybords.profile_kb import profilr_kb
from utils.database import Database
import os

async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id, f'Категорически приветствую {users[1]}!', reply_markup=profilr_kb)
    else:
        await bot.send_message(message.from_user.id, f'Категорически приветствуем в нашем магазине👋 \n'
                                                      f'Бот поможет зарегистрировать аккаунт.✅ \n'
                                                      f'Также возможно просмотреть свою корзину 🗃 \n\n\n', reply_markup=
                           register_keyboard)