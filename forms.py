from aiogram.fsm.state import State, StatesGroup


class TaskStates(StatesGroup):
    """States for task management."""
    waiting_for_text = State()
    waiting_for_time = State()