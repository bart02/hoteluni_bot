from aiogram.dispatcher.filters.state import StatesGroup, State


class SetCleaningReminderStates(StatesGroup):
    set_is_day_before = State()
    enter_campus_number = State()
    enter_time = State()


class OffCleaningReminderStates(StatesGroup):
    enter_campus_number = State()
