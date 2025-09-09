from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('!!!это Юрик дурик')

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help!!!!')

@router.message(F.text == 'Как дела?')
async def get_help(message: Message):
    await message.answer('OK!')

@router.message()
async def echo_message(message):
    await message.answer(text=message.text)
