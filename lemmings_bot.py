# lemmings_bot.py
import cv2
import numpy as np
import pyautogui
from image_processing import load_templates, detect_lemmings_and_goal
from actions import execute_actions, button_coords, click_action
from ai_logic import rule_based_ai
import time

# Define the region to capture (top-left x, top-left y, width, height)
region = (1, 55, 1700, 420)  # Example values, adjust them according to your setup

# Capture the screen in the defined region
screenshot = pyautogui.screenshot(region=region)

# Convert the screenshot to a numpy array and process it
frame = np.array(screenshot)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# Load templates and detect lemmings and goals
lemming_templates, goal_template = load_templates('images')
lemmings, goal, detected_frame = detect_lemmings_and_goal(gray_frame, lemming_templates, goal_template)

# Display detected lemmings and goals
cv2.imshow("Detected Lemmings and Goals", detected_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Function to test clicking the digger button and a lemming
def test_click_digger_on_lemming(lemmings):
    if lemmings:
        # Move to the "digger" button position and click
        pyautogui.moveTo(button_coords["digger"])
        time.sleep(1)  # Wait for 1 second to visually verify the mouse position
        pyautogui.click()
        
        # Delay to ensure the game registers the button click
        time.sleep(0.5)
        
        # Click on the first detected lemming's position
        lemming_position = lemmings[0]
        pyautogui.moveTo(lemming_position)
        time.sleep(1)  # Wait for 1 second to visually verify the mouse position
        pyautogui.click()

        print(f"Clicked 'digger' button and then clicked on lemming at {lemming_position}.")
    else:
        print("No lemmings detected.")

# Run the test
test_click_digger_on_lemming(lemmings)
