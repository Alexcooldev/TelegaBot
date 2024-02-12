from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Зарегистрировать аккаунт'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для получения результата нажми на кнопку ниже')
