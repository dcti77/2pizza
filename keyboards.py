from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_town = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Минск")
        ],
        [
            KeyboardButton(text = "Гомель")
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

purchase_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Заказать", callback_data = "make_order")
        ],
        [
            KeyboardButton(text = "Очистить корзину", callback_data = "cancel_purchase")
        ]

    ]
)
