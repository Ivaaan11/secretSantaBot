import app.keyboards as k
from app.filters import IsAdmin

import logging

from aiogram import F, Router, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()



# stopping the bot

@router.message(IsAdmin(), F.text.casefold() == 'stop')
async def cmd_stop(message: Message, dp: Dispatcher, bot: Bot):
    await message.answer('Stopping the bot...')

    logging.warning('Stopping the bot...')
    await dp.stop_polling()
    await bot.session.close()
    logging.warning('Bot Stopped')