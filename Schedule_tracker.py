# Import necessary libraries
import pretty_errors  # noqa: F401
from dateutil.parser import parse
import winsound
import pandas as pd
from datetime import datetime, timedelta
import locale
from dotenv import dotenv_values
import tkinter as tk
from tkinter import font, messagebox # noqa: F401
import logging
from typing import Optional

# Configure the logging
logging.basicConfig(filename='task_tracker.log', level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

class ExcelReader:
    """
    Class to read and process the Excel file containing the schedule.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_excel(file_path, sheet_name='Horario plus')
        locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

    def get_day_column(self, day: str) -> str:
        """
        Gets the appropriate column name for the given day of the week.

        Args:
            day: The day of the week as a string (e.g., "Montag", "Dienstag").

        Returns:
            The name of the column in the DataFrame corresponding to the given day.
            Defaults to "Time M - F" if the day is not found in the mapping.
        """
        day_columns = {
            "Sonntag": "Time Sontag",
            "Samstag": "Time Samstag",
            "Montag": "Time M - F",
            "Dienstag": "Time M - F",
            "Mittwoch": "Time M - F",
            "Donnerstag": "Time M - F",
            "Freitag": "Time M - F"
        }
        return day_columns.get(day, "Time M - F")

    def get_daily_schedule(self, day: str) -> pd.Series:
        """
        Returns the daily schedule for the given day of the week.

        Args:
            day: The day of the week as a string (e.g., "Montag", "Dienstag").

        Returns:
            A pandas Series containing the time blocks for the given day.
        """
        return self.df[self.get_day_column(day)]

    def get_tasks(self, day: str) -> pd.Series:
        """
        Returns the tasks for the given day of the week.

        Args:
            day: The day of the week as a string (e.g., "Montag", "Dienstag").

        Returns:
            A pandas Series containing the tasks for the given day.
        """
        return self.df[day]

class TaskTracker:
    """
    Main class to handle the task tracking logic and user interface.
    """

    def __init__(self, excel_reader: ExcelReader):
        self.excel_reader = excel_reader
        self.root = tk.Tk()
        self.root.title("Task Tracker")
        self.root.attributes('-topmost', True)
        # self.root.geometry("900x350")
        self.label_font = font.Font(family="Goudy Old Style", size=13)
        self.label_font2 = font.Font(family="Helvetica", size=14)
        self.label_font3 = font.Font(family="Helvetica", size=20)
        self.final_time = "22:31"
        self.current_time = datetime.now().strftime('%H:%M')
        self.today = datetime.now().strftime('%A')
        self.daily_schedule = self.excel_reader.get_daily_schedule(self.today)
        self.tasks = self.excel_reader.get_tasks(self.today)
        self.position = self.get_current_position()
        self.setup_ui()


    def get_current_position(self) -> Optional[int]:
        """
        Finds the position of the current task in the schedule.

        Returns:
            The position (index) of the current task in the schedule, or None if not found.
        """
        time_block = self.look_the_time()
        if time_block is not None:
            for i, block in enumerate(self.daily_schedule):
                if block == time_block:
                    return i
        return None

    def look_the_time(self) -> Optional[str]:
        """
        Finds the current time block in the schedule.

        Returns:
            The time block string if found in the schedule, or None if not found.
        """
        for block in self.daily_schedule:
            # Check if the block is a string before splitting
            if isinstance(block, str): 
                start, end = block.split(" - ")
                start_time = parse(start, fuzzy=True).time()
                end_time = parse(end, fuzzy=True).time()
                current_time = datetime.now().time()
                if start_time <= current_time < end_time:
                    return block
        return None
    



    def setup_ui(self):
        """
        Sets up the user interface elements.
        """
        self.label1 = tk.Label(self.root, text="Heutiger Tag:", font=self.label_font)
        self.label1.pack()

        self.label2 = tk.Label(self.root, text=self.today, font=self.label_font2)
        self.label2.pack()

        self.label3 = tk.Label(self.root, text="Aktuelle Uhrzeit:", font=self.label_font)
        self.label3.pack()

        self.label4 = tk.Label(self.root, text=self.current_time, font=self.label_font2)
        self.label4.pack()

        self.label5 = tk.Label(self.root, text="Aktuelle Aufgabe:", font=self.label_font)
        self.label5.pack()
        
                # Pause button
        self.schedule_button = tk.Button(self.root, text="show schedule", command=self.toggle_schedule)
        self.schedule_button.pack(padx=10, pady=5, side="left")

        if self.position is not None:
            self.label6 = tk.Label(self.root, text=self.tasks.iloc[self.position], font=self.label_font3, wraplength=400, fg="green")
        else:
            self.label6 = tk.Label(self.root, text="Keine Aufgabe gefunden", font=self.label_font3, wraplength=400)
        self.label6.pack()

        self.update_time()
        self.root.mainloop()   
    
    
            
    def toggle_schedule(self):
        """
        Toggles the visibility of the complete schedule.
        """
        if hasattr(self, "schedule_window"):
            # If the schedule window already exists, destroy it
            self.schedule_window.destroy()
            del self.schedule_window
            self.schedule_button.config(text="Show Schedule")
        else:
            # Otherwise, create the schedule window
            self.show_schedule()
            self.schedule_button.config(text="Hide Schedule")

    def show_schedule(self):
            # Create a new window
            self.schedule_window = tk.Toplevel(self.root)
            self.schedule_window.title("Complete Schedule")
            self.schedule_window.attributes('-topmost', True) 

            # Add a label for each time block and task
            self.schedule_labels = []
            for i, (time_block, task) in enumerate(zip(self.daily_schedule, self.tasks)):
                if pd.isna(task):
                    continue
                label_text = f"{time_block}: {task}"
                label = tk.Label(self.schedule_window, text=label_text)

                # Highlight the current task
                if i == self.position:
                    label.config(bg="yellow")

                label.pack()
                self.schedule_labels.append(label)      
            
    def update_time(self):
        """
        Updates the current time label every second.
        """
        self.current_time = datetime.now().strftime('%H:%M')
        self.label4.config(text=self.current_time)
        if self.current_time == self.final_time:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        # Check if it's 5 minutes before the end of the current task
        if self.position is not None:
            _, end = self.daily_schedule.iloc[self.position].split(" - ")
            end_time = (parse(end, fuzzy=True) - timedelta(minutes=5)).strftime('%H:%M')
            if self.current_time == end_time:
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  # Play a sound
                

        # Update the schedule labels
        if hasattr(self, "schedule_labels"):
            for i, label in enumerate(self.schedule_labels):
                if i == self.position:
                    label.config(bg="yellow")
                else:
                    label.config(bg=self.schedule_window.cget("bg"))
        self.root.after(30000, self.update_time)

if __name__ == "__main__":
    config = dotenv_values(".env")
    excel_file = config.get("CALENDAR_FILE_PATH")
    if excel_file:
        reader = ExcelReader(excel_file)
        app = TaskTracker(reader)
    else:
        logging.error("Excel file path not found in the environment variables.")

