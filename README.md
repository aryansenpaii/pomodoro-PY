# Pomodoro Timer

A simple Pomodoro Timer application built using Python and the Tkinter module. This application helps you manage time using the Pomodoro technique by alternating between work intervals, short breaks, and long breaks, with a visual check mark system to track progress.


## Features

- **Start Button**: Begins a Pomodoro session.
- **Reset Button**: Resets the timer to zero.
- **Work Sessions**: Default work time is set to 25 minutes.
- **Short Breaks**: Short break of 5 minutes between work sessions.
- **Long Breaks**: A 20-minute long break after four work sessions.
- **Check Mark System**: Displays a check mark at the bottom of the window after each completed Pomodoro set (one work session + one short break).
- Tomato-themed timer for an engaging look.
  
## How to Use

1. **Start the Timer**: Click the "Start" button to begin a Pomodoro session (25-minute work session).
2. **Reset the Timer**: Use the "Reset" button to reset the timer at any time.
3. **Check Marks**: After each work and short break set, a check mark will appear, helping you track your progress.
4. **Long Break**: After four Pomodoro sets (four work sessions + four short breaks), the timer will automatically provide a long break of 20 minutes.

## Installation

To use the Pomodoro Timer, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pomodoro-PY.git
   cd pomodoro-PY
   ```

2. Install the required dependencies:

   Tkinter comes pre-installed with Python. Make sure you have Python installed. Download Python from [here](https://www.python.org/downloads/) if needed.

3. Run the application:

   ```bash
   python pomodoro_timer.py
   ```

## Customization

You can customize the session durations by modifying these variables in `pomodoro_timer.py`:

```python
WORK_MIN = 25  # Work session length in minutes
SHORT_BREAK_MIN = 5  # Short break length in minutes
LONG_BREAK_MIN = 20  # Long break length in minutes
```

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to update the `path_to_screenshot_image.png` with the correct path for your screenshot, and let me know if you need any further adjustments!
