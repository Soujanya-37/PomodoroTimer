🍅 PomodoroTimer: A Command-Line Productivity Tool

This is a simple, feature-rich Pomodoro timer that runs directly in your command line or terminal. It's built with standard Python and requires no external libraries.

It's a perfect tool to help you stay focused on your work or studies by breaking your time into focused sessions and breaks.

✨ Features

🚀 Core Functionality

Customizable Times: At the start, you can set your own durations for Pomodoros, short breaks, and long breaks, or just press Enter to use the defaults (25, 5, 15).

Classic Pomodoro Workflow: Follows the standard 4-cycle workflow (Pomodoro, Short Break, Pomodoro, Short Break, Pomodoro, Short Break, Pomodoro, Long Break).

Skip Timers: You can press Ctrl+C during any timer (work or break) to skip it and move to the next session.

🎨 Command-Line UI

Clean Terminal Display: The timer updates on a single, dynamic line, keeping your terminal window clean.

Simple Alarm: Plays a terminal "bell" sound (the \a character) when a session is complete.

Interactive Prompts: Clearly guides you when to start your next work session or break.

🛠️ Technologies Used

Python 3

Built-in Modules:

time (for time.sleep())

sys (for sys.stdout.write)

🚀 How to Run

Open your Command Prompt (cmd) or Terminal.

Navigate to the folder where you saved the file (e.g., your Downloads folder):

cd C:\Users\shanb\Downloads


Run the script using Python:

python pomodoro_timer.py


That's it! The program will guide you from there.

📖 How to Use

When the script starts, it will ask you to set durations for the Pomodoro, short break, and long break. Press Enter to accept the defaults (25, 5, 15) or type your own values (in minutes) and press Enter.

Press Enter to start the first Pomodoro session.

The timer will count down on a single line.

To skip a session (work or break) at any time, press Ctrl+C.

To quit the entire program, press Ctrl+C at one of the "Press Enter to start..." prompts.

🎯 Core Concepts Implemented

User Input: Getting custom times and start/stop commands from the user via input().

Time Management: Using the time.sleep() function to pause the program for one-second intervals, creating the countdown.

Dynamic Terminal Output: Using sys.stdout.write and the carriage return \r to overwrite the current line in the terminal, creating a smooth, single-line timer.

Exception Handling: Using try...except KeyboardInterrupt to gracefully handle Ctrl+C as a feature (to skip timers or exit) rather than crashing the program.

Looping & State: Managing the 4-cycle workflow with a for loop and tracking the current session number.

📄 License

Distributed under the MIT License. (You can add a LICENSE file to your repository if you wish, but this is a good placeholder).

🙏 Acknowledgments

A 1st year Python project by Soujanya Shanbhag.
