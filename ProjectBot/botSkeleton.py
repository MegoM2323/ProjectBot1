import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import BotParser

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


################################################################################################################
#Основа
bot = Bot(token='1793275901:AAF0G2aQyXeGcmbQbfGVQKTpgen1vt0_13Q')
dp = Dispatcher(bot)
CHENAL_ID = -1001428325485
################################################################################################################
# клавиатура
btnRandom = KeyboardButton("/Рандомное")
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnRandom)
################################################################################################################

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo_message(msg: types.Message):
    if msg.text != None or "None":
        await bot.send_message(CHENAL_ID, msg.text)
    #print(BotParser.Gmessage)


if __name__ == '__main__':
    executor.start_polling(dp)

'''
from pyrogram import Client, filters  # телеграм клиент

API_ID = 7906995
API_HASH = '6d2cf947c1caaece9fb2fb50db17a363'

PUBLIC_PUBLIC = 'IT Энергия'  # паблик куда будем репостить

SOURCE_PUBLICS = [
    # список пабликов-доноров, откуда бот будет пересылать посты
    'andro-price.com',
    'Alexandr Semak - СКИДКИ и ОБЗОРЫ на гаджеты',
]
PHONE_NUMBER = '89170493967'  # номер зарегистрованный в телеге

# создаем клиент телеграм
app = Client("cyberpunk", api_id=API_ID, api_hash=API_HASH,
             phone_number=PHONE_NUMBER)


@app.on_message()
async def hello(client, message):
    print(message.text) # Выводим в консоль
'''
################################################################################################################3







"""
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup= mainMenu)\

@dp.message_handler(commands=['Рандомное'])
async def process_start_command(message: types.Message):
    await message.reply(random.randint(123,12341234))


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
"""