import pyautogui
import time

# Function to get current mouse position
def get_mouse_position():
    return pyautogui.position()

# Function to click at given coordinates
def click_button(coords):
    pyautogui.moveTo(coords)
    time.sleep(1)  # Short delay for visual confirmation
    pyautogui.click()
    print(f"Clicked at coordinates: {coords}")

# Main script
print("Move your mouse to the Digger button and press Enter")
input("Press Enter when ready...")

digger_coords = get_mouse_position()
print(f"Recorded Digger button coordinates: {digger_coords}")

input("Press Enter to click the Digger button...")
click_button(digger_coords)

print("Script completed")