from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Reply-клавиатура с кнопками "Привет" и "Пока"
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
    ],
    resize_keyboard=True
)

# Инлайн-клавиатура с URL-ссылками
inline_links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.ycombinator.com/")],
        [InlineKeyboardButton(text="Музыка", url="https://spotify.com/")],
        [InlineKeyboardButton(text="Видео", url="https://youtube.com/")],
    ]
)

# Динамическая инлайн-клавиатура (начальная кнопка)
dynamic_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
    ]
)

# Динамическая инлайн-клавиатура (опции)
dynamic_options_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")],
    ]
)

# Тестовая клавиатура с кнопками, ведущими на ссылки
test = ["Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4"]

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, url="https://www.youtube.com/"))
    return keyboard.adjust(2).as_markup()
