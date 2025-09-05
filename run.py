import aiogram
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token='8095790596:AAFsZ5-TIGMDZ8Ki6LhrOPe1FENhLAC-sdQ')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('это Юрик дурик')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
