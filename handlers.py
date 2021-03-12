from main import bot, dp

from aiogram.types import Message, ReplyKeyboardRemove
from config import admin_id
from keyboards import menu_town, menu_town_pizza
from aiogram.dispatcher.filters import Command, Text

#@dp.message_handler(Command())

@dp.message_handler(Command("start"))
async def choose_town(message: Message):
     await message.answer("Выбери свой гороод", reply_markup=menu_town)

@dp.message_handler(Text(equals=["Минск","Гомель"]))
async  def pizza_in_town(message: Message):
    await message.answer("Выберите пиццерию в вашем городе",reply_markup=menu_town_pizza)



