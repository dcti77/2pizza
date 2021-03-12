from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_town = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Минск")
        ],
        [
            KeyboardButton(text =  "Гомель")
        ],
    ],
    resize_keyboard=True
)

menu_town_pizza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Papa John's")
        ],
        [
            KeyboardButton(text = "Dominos")
        ],
        [
            KeyboardButton(text = "Dodo pizza")
        ],
    ],
)
