from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6935015637:AAFWVj_siPpTJ98EkIYoaeG8VsZv5nf-re0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет! Напиши мне что-нибудь)")
   
@dp.message_handler() 
async def echo(message: types.Message):
   await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)