import asyncio

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from forms import TaskStates
from db import save_reminder


router = Router()


async def reminder_task(message: Message, text: str, delay: int) -> None:
    """Background task to send a reminder after a delay."""
    await asyncio.sleep(delay * 60)
    await message.answer(f"Reminder: {text}")


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    """Handler for the /start command."""
    await message.answer("Welcome! Please enter the task you want to be reminded about:")
    await state.set_state(TaskStates.waiting_for_text)


@router.message(TaskStates.waiting_for_text)
async def text_handler(message: Message, state: FSMContext) -> None :
    """Handler for receiving the task text."""
    await state.update_data(text=message.text)
    await message.answer("Great! Now enter the time in minutes after which you want to be reminded.")
    await state.set_state(TaskStates.waiting_for_time)


@router.message(TaskStates.waiting_for_time)
async def time_handler(message: Message, state: FSMContext) -> None:
    """Handler for receiving the reminder time."""
    if not message.text.isdigit():
        await message.answer("Please enter a valid number for the time in minutes.")
        return
    
    delay = int(message.text)
    await state.update_data(delay=delay)

    user_data = await state.get_data()
    await save_reminder(message.from_user.id, user_data['text'], user_data['delay'])

    await message.answer(f"Reminder set! I'll remind you about '{user_data['text']}' in {delay} minutes.")
    await state.clear()

    asyncio.create_task(reminder_task(message, user_data['text'], delay))