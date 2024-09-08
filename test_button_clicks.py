# test_button_clicks.py
import pyautogui
import time

# Define button coordinates
button_coords = {
    "climber": (24, 442),
    "floater": (70, 442),
    "exploder": (112, 442),
    "blocker": (156, 442),
    "builder": (201, 442),
    "basher": (250, 442),
    "miner": (288, 442),
    "digger": (333, 442)
}

def test_button_clicks(button_coords):
    """Test clicking each action button."""
    for action, coords in button_coords.items():
        print(f"Clicking '{action}' button at {coords}...")
        pyautogui.moveTo(coords)  # Move to the button
        time.sleep(1)  # Wait for 1 second to confirm the mouse is in position
        pyautogui.click()  # Click the button
        time.sleep(1)  # Wait for 1 second between clicks

# Ensure the game window is focused and run the test
print("Make sure the game window is focused. Starting button click test...")
time.sleep(3)  # Give the user time to focus the game window

test_button_clicks(button_coords)
print("Button click test completed.")
