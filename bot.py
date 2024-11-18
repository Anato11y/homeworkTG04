import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboard as kb

# Укажите токен вашего Telegram-бота
TOKEN = "7712311127:AAEIGmbL0Ozl0rqiDbLkA8KPCJ6NKCExzIs"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Приветики, {message.from_user.first_name}!",
        reply_markup=kb.main
    )

# Обработчик команд /help
@dp.message(Command("help"))
async def help_command(message: Message):
    commands = """
Доступные команды:
- /start - Запустить бота и отобразить меню
- /help - Отобразить список доступных команд
- /links - Показать ссылки на полезные ресурсы
- /dynamic - Показать динамическое меню
"""
    await message.answer(commands)
# Обработчик нажатия кнопок "Привет" и "Пока"
@dp.message(F.text.in_({"Привет", "Пока"}))
async def handle_main_menu(message: Message):
    if message.text == "Привет":
        await message.answer(f"Привет, {message.from_user.first_name}!")
    elif message.text == "Пока":
        await message.answer(f"До свидания, {message.from_user.first_name}!")

# Обработчик команды /links
@dp.message(Command("links"))
async def links_command(message: Message):
    await message.answer("Полезные ссылки:", reply_markup=kb.inline_links_keyboard)

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    await message.answer("Выберите опцию:", reply_markup=kb.dynamic_start_keyboard)

# Обработчик callback-кнопок для динамического меню
@dp.callback_query()
async def handle_dynamic(callback: CallbackQuery):
    if callback.data == "show_more":
        await callback.message.edit_text("Выберите опцию:", reply_markup=kb.dynamic_options_keyboard)
    elif callback.data == "option_1":
        await callback.message.answer("Вы выбрали Опцию 1.")
    elif callback.data == "option_2":
        await callback.message.answer("Вы выбрали Опцию 2.")

# Обработчик нажатия на кнопку "Новости"
@dp.callback_query(F.data == "news")
async def news_callback(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text("Вот свежие новости!", reply_markup=await kb.test_keyboard())

# Основная функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
