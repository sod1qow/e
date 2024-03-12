from utils.loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.reply_btn import start_menu, evos_btn, feedback_btn, settings_btn, translet_btn





@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    btn = await start_menu()
    await message.answer(f'Выберите одно из следующих',reply_markup=btn)




@dp.message_handler(text='🍴 Меню')
async def menu_foods(message: Message):
  btn = await evos_btn()
  await message.answer("Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=btn)




@dp.message_handler(text='🛍 Мои заказы')
async def zakaz_foods(message: Message):
  await message.answer("Вы совсем ничего не заказали.")


@dp.message_handler(text='✍️ Оставить отзыв')
async def feedback_foods(message: Message):
  btn = await feedback_btn()
  await message.answer("Отправьте ваши отзывы", reply_markup=btn)



@dp.message_handler(text='⚙️ Настройки')
async def settings_foods(message: Message):
  btn = await settings_btn()
  await message.answer("Выберите действие:", reply_markup=btn)



@dp.message_handler(text='Изменить язык')
async def download_foods(message: Message):
  btn = await translet_btn()
  await message.answer("Выберите язык:", reply_markup=btn)



@dp.message_handler(text='🗺 Мои адреса')
async def adres_foods(message: Message):
  await message.answer("Пусто")



@dp.message_handler(text='🔙 ortga')
async def back_handler(message: Message):
  await start_bot(message)






