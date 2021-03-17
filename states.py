from aiogram.dispatcher.filters.state import StatesGroup, State

class NamePhone(StatesGroup):
    QName = State()
    QPhone = State()
