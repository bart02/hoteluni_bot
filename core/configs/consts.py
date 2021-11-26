"""
This file is created for config which is not depends on a particular project
and you won't need to specify them, but vars from here are used in other configs
"""
from datetime import date, timedelta
from pathlib import Path

import pytz

BASE_DIR: Path = Path().cwd()
LOGS_FOLDER: Path = BASE_DIR / "logs"

base_dates_campus_cleaning = {
    1: [date(2020, 8, 31), date(2020, 9, 9), date(2020, 9, 18), None],
    '2 (1-2)': [date(2020, 9, 4), None, date(2020, 9, 14), date(2020, 9, 23)],
    '2 (3-4)': [date(2020, 9, 4), None, date(2020, 9, 14), date(2020, 9, 23)],
    3: [None, date(2020, 9, 7), date(2020, 9, 16), date(2020, 9, 25)],
    4: [date(2020, 9, 2), date(2020, 9, 11), None, date(2020, 9, 21)],
}  # campus_number -> some day with cleaning
cleaning_interval = 28
default_timezone = pytz.timezone("Europe/Moscow")
job_id_format = "cleaning_reminder:{chat_id}:{campus_number}:{index}"
