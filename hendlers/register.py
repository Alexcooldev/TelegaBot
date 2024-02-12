from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database

async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if(users):
        await bot.send_message(message.from_user.id, f'{users[1]} \n Ты уже часть легиона')
    else:
        await bot.send_message(message.from_user.id, f'🌚Начием регистрацию? \n Для начала назови свое погоняло.🌚')
        await state.set_state(RegisterState.regName)

async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id,f'😏 Ну, здорова коль не шутиш {message.text}\n'
                         f'☎️ А теперь напиши номер телефона для того, чтобы быть на связи \n'
                         f'📲 Формат номера +375 хх ххх хх хх \n\n'
                         f'⚠️ ВНИМАНИЕ!!! Я очень чувствителен к формату')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)

async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if (re.findall('^\+?[375][-\(]?\d{2}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = f'Будем знакомы {reg_name}\n\n Номерок - {reg_phone}'
        await bot.send_message(message.from_user.id,msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()

    else:
        await bot.send_message(message.from_user.id, f'❌Номер указан в неверном формате❌')