from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_menu():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("🍴 Меню")
    btn.row("🛍 Мои заказы")
    btn.row("✍️ Оставить отзыв", "⚙️ Настройки")
    
    return btn


async def evos_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("🗺 Мои адреса", "📍 Отправить геолокацию")
    btn.row("⬅️ Назад")

    return btn



async def feedback_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.row("⬅️ Назад")

    return btn



async def settings_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add("Изменить язык")
    btn.add("⬅️ Назад")

    return btn



async def translet_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")
    btn.add("⬅️ Назад")

    return btn




