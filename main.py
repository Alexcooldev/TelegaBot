from aiogram import Bot, Dispatcher, types, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import CommandStart, Command
from utils.commands import set_command
from hendlers.start import get_start
from state.register import RegisterState
from hendlers.register import start_register, register_name, register_phone
from filters.CheckAdmin import CheckAdmin

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

dp.message.register(get_start, Command(commands='start'))

dp.message.register(start_register, F.text == 'Зарегистрировать аккаунт')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await bot.send_message(6679431895, 'Бот запущен')

async def main()->None:
    await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())

