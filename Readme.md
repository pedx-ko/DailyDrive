📚 Task Tracker: Your Personal Daily Planner 🗓
==================================================

🧑‍💻 Project Description
-------------------------

Welcome to the Task Tracker, a Python-based application designed to help you stay focused and organized by managing your daily tasks efficiently. The goal of this project is to enable you to view your scheduled tasks at specific times while you're at home, making the most of your time.


🚀 **Task Tracker Step-by-Step Guide** 🚀

This project helps you stay on top of your daily tasks by displaying your current task and alerting you when the end of each time block approaches.

**1. ⚙️ Environment Setup:**

* 🐍 **Install Python:** If you don't have it yet, download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* 📚 **Required Libraries:** 
    - **pandas:** For reading and processing data from Excel.
    - **tkinter:** For creating the graphical user interface.
    - **dateutil, datetime:** For working with dates and times.
    - **dotenv:** For loading environment variables.

**2. 📅 Prepare Your Schedule:**

* 📊 **Excel File:** Create an Excel file (`.xlsx`) with two important columns:
    - **"Time M - F" (or other columns for specific days):** Time blocks in the format "HH:MM - HH:MM" (e.g., "09:00 - 10:30").
    - **Day of the week name (e.g., "Monday"):** Tasks corresponding to each time block.
* 🤫 **`.env` File (Optional):** You can store the path to your Excel file in a `.env` file to keep it separate from your code.

**3. 🏃 Run the Code:**

* 💻 **Open the Python File:** Open the `task_tracker.py` file in your favorite code editor or IDE.
* ▶️ **Run:** Press "Run" (or use the keyboard shortcut) to start the application.

**4. 🖥️ User Interface:**

* ⏰ **Information:** The window will display:
    - The current day of the week.
    - The current time.
    - The task you should be working on right now.
* 🔊 **Alerts:**
    - 5 minutes before a task ends, you'll hear a sound.
    - At the end time, another sound will play.
* 👀 **"Show Schedule" Button:** Click to see your complete schedule.
* ❌ **"Exit" Button:** Close the application.

**5. 🤔 How It Works:**

* 🧐 **Schedule Reading:** The code reads your schedule from the Excel file.
* 🔍 **Current Task Lookup:** It determines which time block you're in and what the corresponding task is.
* 🔄 **Constant Update:** The current time and task are updated every 30 seconds.
* ⏰ **Scheduled Alerts:** Alerts are scheduled using `root.after()`.

**6. 🛠️ Customization:**

* 🎨 **Fonts:** You can change the fonts in `self.label_font`, `self.label_font2`, etc.
* 🔔 **Sounds:** Replace "SystemExit" with the names of your own sound files.
* 🗓️ **Schedule Format:** Ensure the time blocks in your Excel are in the correct format.
* ➕ **More Features:**
    - You could add a button to pause/resume the timer.
    - You could display the current time block along with the task.

**🎉 Enjoy your personalized Task Tracker! 🎉**

**Example `.env` File:**

```
CALENDAR_FILE_PATH=C:/path/to/your/file.xlsx
```

