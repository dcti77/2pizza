import asyncio

from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from main import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.types import (Message, ReplyKeyboardRemove, InlineKeyboardMarkup,
                           InlineKeyboardButton, CallbackQuery)
from config import admin_id
from keyboards import menu_town, menu_town_pizza, purchase_menu
from aiogram.dispatcher.filters import Command, Text
from states import NamePhone
from sendemail import sendmail

wishlist = []
name = []
phone = []

#Хэндлер для выбора городв, запускается по /start

@dp.message_handler(Command("start"))
async def choose_town(message: Message):
     await message.answer("Выбери свой город", reply_markup=menu_town)

#Хэндлер для выбора в пиццерии

@dp.message_handler(Text(equals=["Минск","Гомель"]))
async def pizza_in_town(message: Message):
    await message.answer("Выберите пиццерию в вашем городе",reply_markup=menu_town_pizza)

# Обработка имени и номера телефона (машина состояний)

@dp.message_handler(Text(equals=["Заказать"]), state= None)
async def pizza_purhcase(message:Message):
    await message.answer("Введите ваше имя")
    await NamePhone.QName.set()
    name.append(message.text)

@dp.message_handler(state = NamePhone.QName)
async def answer_name(message: Message, state: FSMContext):
    name.append(message.text)
    await message.answer("Введите номер телефона")
    await NamePhone.next()

@dp.message_handler(state = NamePhone.QPhone)
async def answer_phone(message: Message, state: FSMContext):
    phone.append(message.text)
    await message.answer(f"Отлично {name} {phone} ваш заказ обрабатывается")
    await state.finish()
    sendmail(msg = (name + phone + wishlist))


#Хэндлер для коллбек запроса инлайн кнопки "оформить заказ"
@dp.callback_query_handler(lambda c: c.data == "make_order")
async def process_make_order(Message: Message):
    await bot.send_message("Вы заказали:")
    pass

#Хэндлер для коллбек запроса инлайн кнопки "купить"

@dp.callback_query_handler(lambda c: c.data == "buy_pizza")
async def process_callback_buy_item(callback_query: CallbackQuery):
    w = callback_query.values["message"].caption
    pizza_name = w.split(".",1)[0]
    wishlist.append(pizza_name)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали пиццу {pizza_name}")

#Хэндлер для коллбек запроса инлайн кнопки "купить"

@dp.callback_query_handler(lambda c: c.data == "cancel_purchase")
async def process_callback_cancel_purchase(callback_query: CallbackQuery):
    wishlist.clear()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы отменили все покупки")

@dp.message_handler(Text(equals="Очистить корзину"))
async def process_callback_cancel_purchase(message: Message):
    wishlist.clear()
    await message.answer("Вы отменили все покупки")

#Хэндлер для коллбек запроса кнопки "корзина"

@dp.callback_query_handler(lambda c: c.data == "purchase")
async def process_callback_show_purchase(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text= "Сейчас у вас в корзине:", reply_markup = purchase_menu)
    for w in wishlist:
        await bot.send_message(callback_query.from_user.id, text = w)



#Хэндлер для предоставления ботом списка блюд с инлайн клавиатурами для выбора пиццы в Доминос

@dp.message_handler(Text(equals=["Dominos"]))
async def show_pizzas_papa(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Купить 1шт", callback_data="buy_pizza"),
            ],
            [
                InlineKeyboardButton(text="Корзина", callback_data="purchase"),
            ],
            [
                InlineKeyboardButton(text="Отменить покупки", callback_data="cancel_purchase"),
            ],
        ]
    )
    await message.answer_photo(
        photo = "https://images.dominos.by/media/dominos/osg/api/2018/09/12/carbonara.png",
        caption = ("Карбонара. \n10,99 руб\nСостав: лук, бекон, крем фреш, ветчина, шампниньоны, сыр моцарелла"),
        reply_markup = markup
    )

    await asyncio.sleep(0.3)

    await message.answer_photo(
        photo="https://images.dominos.by/media/dominos/osg/api/2020/11/18/chiken_fresh_small.png",
        caption=("Чикен Ранч. \n15,49 руб\nСостав: Соус Чесночный, Томаты, Сыр моцарелла, Курица"),
        reply_markup=markup
    )
    await asyncio.sleep(0.3)

    await message.answer_photo(
        photo="https://images.dominos.by/media/dominos/osg/api/2020/03/11/govyadina_burger_small.png",
        caption=("Говядина BURGER. \n15.49 руб\nСостав: Шампиньоны, Телятина, Сыр моцарелла, Соус Бургер, Лук, Огурцы"),
        reply_markup=markup
    )

    await asyncio.sleep(0.3)

    await message.answer_photo(
        photo="https://images.dominos.by/media/dominos/osg/api/2018/09/12/5_syrov.png",
        caption=("5 Сыров. \n17.49  руб\nСостав: Пармезан, Крем фреш, Чеддер, Голубой сыр, Фета, Сыр моцарелла"),
        reply_markup=markup
    )

