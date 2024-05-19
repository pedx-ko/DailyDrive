# Import necessary libraries
import pretty_errors
from dateutil.parser import parse
import winsound
import pandas as pd
from datetime import datetime, timedelta
import locale
from dotenv import dotenv_values
import tkinter as tk
from tkinter import font, messagebox
import logging



# Load environment variables
secre = dotenv_values(".env")
file_path = secre['CALENDAR_FILE_PATH']

# Read the schedule from the Excel file
df = pd.read_excel(file_path, sheet_name='Horario plus')

# Set the locale to Germany
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

# Get the current date and time
now = datetime.now()
today = now.strftime('%A')
current_time = now.strftime('%H:%M')

def get_day_column(day):
    """
    Gets the appropriate column name for the given day of the week.

    Args:
        day: The day of the week as a string (e.g., "Montag", "Dienstag").

    Returns:
        The name of the column in the DataFrame corresponding to the given day.
        Defaults to "Time M - F" if the day is not found in the mapping.
    """
    day_columns = {
        "Sonntag": "Time Sontag",  # Mapping for Sunday
        "Samstag": "Time Samstag",  # Mapping for Saturday
        "Montag": "Time M - F",    # Mapping for Monday (and weekdays)
        "Dienstag": "Time M - F",  # Mapping for Tuesday
        "Mittwoch": "Time M - F",  # Mapping for Wednesday
        "Donnerstag": "Time M - F",  # Mapping for Thursday
        "Freitag": "Time M - F"   # Mapping for Friday
    }
    return day_columns.get(day, "Time M - F")  # Default to "Time M - F" if day not found

daily_schedule = df[get_day_column(today)]

# Get the tasks column for the current day of the week
tasks = df[today]

def look_the_time():
    '''this function find the current block time'''
    for time_block in daily_schedule:
        start_time, end_time = [t.strip() for t in time_block.split('-')]
        if start_time <= current_time <= end_time:
            # Check if the time block is found in the DataFrame
            if df[daily_schedule == time_block].size > 0:
                return time_block
            else:
                logging.error(f"Time block '{time_block}' not found in the DataFrame.")
                return None
    # If no time block is found, return None
    logging.error(f"No time block found for the current time '{current_time}'.")
    return None


print(daily_schedule)
print(tasks)

now = datetime.now()
current_time = now.strftime('%H:%M')
time_block = look_the_time()
# print(current_time)
# find and  the position of the current task
if not daily_schedule.empty and daily_schedule[daily_schedule == time_block].index.size > 0:
    position = df[daily_schedule == time_block].index[0]  
# Rest of your code
else:
    logging.error(f"No data found for time block '{time_block}' in the DataFrame.")

# print(position)