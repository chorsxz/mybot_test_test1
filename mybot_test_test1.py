import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

# Токен бота
bot = Bot(token="7039598908:AAG2gX-34zGxvICM8RhWuPIWrERRq6ZmdCU")
dp = Dispatcher()

# handler /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!!! HI!!!! my sweet Stepovyata")

# handler /test
@dp.message(Command("test"))
async def test(message: types.Message):
    await message.answer("test 1")

# Основна функція
async def main():
    await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
