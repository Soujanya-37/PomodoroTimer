import time
import sys
import os

# --- Default Constants ---
DEFAULT_POMODORO_MINS = 25
DEFAULT_SHORT_BREAK_MINS = 5
DEFAULT_LONG_BREAK_MINS = 15

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen."""
    # 'nt' is for Windows, 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def play_alarm_sound():
    """Prints the 'bell' character to the terminal as a simple alarm."""
    # \a is the "alert" or "bell" character
    print("\a")

def get_custom_times():
    """
    Asks the user to set custom timer durations or use defaults.
    Returns a tuple of (pomodoro_mins, short_break_mins, long_break_mins)
    """
    print("--- Customize Your Timer (Press Enter to use defaults) ---")
    
    try:
        # Get Pomodoro time
        pomo_input = input(f"  Pomodoro duration ({DEFAULT_POMODORO_MINS} mins): ")
        pomodoro_mins = int(pomo_input) if pomo_input else DEFAULT_POMODORO_MINS
        
        # Get Short Break time
        short_input = input(f"  Short break duration ({DEFAULT_SHORT_BREAK_MINS} mins): ")
        short_break_mins = int(short_input) if short_input else DEFAULT_SHORT_BREAK_MINS
        
        # Get Long Break time
        long_input = input(f"  Long break duration ({DEFAULT_LONG_BREAK_MINS} mins): ")
        long_break_mins = int(long_input) if long_input else DEFAULT_LONG_BREAK_MINS
        
        print("----------------------------------------------------------")
        return pomodoro_mins, short_break_mins, long_break_mins
        
    except ValueError:
        print("Invalid input. Please enter numbers only. Using defaults.")
        print("----------------------------------------------------------")
        return DEFAULT_POMODORO_MINS, DEFAULT_SHORT_BREAK_MINS, DEFAULT_LONG_BREAK_MINS
    except KeyboardInterrupt:
        print("\nSetup cancelled. Exiting.")
        sys.exit(0)


def run_timer(minutes, mode_name):
    """
    Runs a countdown timer for a given number of minutes.
    
    Args:
        minutes (int): The duration of the timer in minutes.
        mode_name (str): The name of the current mode (e.g., "Pomodoro").
    """
    total_seconds = minutes * 60
    
    print(f"\nStarting {mode_name} for {minutes} minutes.")
    print("Press Ctrl+C to skip this timer.")
    
    try:
        # Loop until the time is up
        while total_seconds > 0:
            try:
                # 1. Calculate remaining minutes and seconds
                # divmod() is a handy function that returns both the quotient and remainder
                mins_left, secs_left = divmod(total_seconds, 60)
                
                # 2. Create the time display string
                # :02d formats the number to 2 digits, padding with a 0 if needed
                time_string = f"{mins_left:02d}:{secs_left:02d}"
                
                # 3. Print the time to the same line
                # \r (carriage return) moves the cursor to the start of the line
                # end="" prevents it from printing a newline character
                # sys.stdout.flush() forces the output to display immediately
                sys.stdout.write(f"\r  {mode_name} | Time Remaining: {time_string}  ")
                sys.stdout.flush()
                
                # 4. Wait for one second
                time.sleep(1)
                
                # 5. Decrement the time
                total_seconds -= 1
                
            except KeyboardInterrupt:
                # Handle user pressing Ctrl+C *during* the timer
                print("\n\nTimer skipped! Moving to the next session.")
                play_alarm_sound() # Give a little sound on skip
                return # Exit the function early
            
        # Timer finished normally
        print("\n\n" + "="*30)
        print(f"  {mode_name} Complete!")
        print("="*30)
        play_alarm_sound()

    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


# --- Main Application Logic ---

def main():
    """
    The main function to run the Pomodoro workflow.
    """
    clear_screen()
    print("--- Python Pomodoro Timer ---")
    
    # Get timer durations from the user
    pomo_mins, short_break_mins, long_break_mins = get_custom_times()
    
    pomodoro_count = 0
    
    try:
        while True:
            # --- 1. Run Pomodoro Session ---
            run_timer(pomo_mins, "Pomodoro")
            pomodoro_count += 1
            print(f"  You've completed {pomodoro_count} Pomodoro(s).")
            
            # --- 2. Determine Break Type ---
            if pomodoro_count % 4 == 0:
                # Time for a long break
                print("\nTime for a long break!")
                input(f"  Press Enter to start your {long_break_mins}-minute long break... ")
                run_timer(long_break_mins, "Long Break")
            else:
                # Time for a short break
                print("\nTime for a short break!")
                input(f"  Press Enter to start your {short_break_mins}-minute short break... ")
                run_timer(short_break_mins, "Short Break")
            
            # --- 3. Prepare for next session ---
            print("\nBreak finished!")
            input("  Press Enter to start the next Pomodoro (Ctrl+C to quit)... ")
            clear_screen()

    except (KeyboardInterrupt, EOFError):
        # Handle Ctrl+C or Ctrl+D at the "Press Enter" prompts to exit
        print("\n\nPomodoro app closing. Great work!")
        sys.exit(0)

# Standard Python entry point
if __name__ == "__main__":
    main()

