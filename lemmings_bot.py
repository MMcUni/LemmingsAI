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
def predictive_click_lemming(lemmings, region, movement_speed=2):
    if lemmings:
        # Click the digger button
        pyautogui.click(button_coords["digger"])
        
        # Get the lemming's position
        lemming_x, lemming_y = lemmings[0]
        
        # Predict the new position based on assumed movement
        predicted_x = lemming_x + movement_speed
        
        # Adjust coordinates based on the capture region
        screen_x = region[0] + predicted_x
        screen_y = region[1] + lemming_y
        
        # Click on the predicted position
        pyautogui.click(screen_x, screen_y)
        
        print(f"Clicked 'digger' button and then clicked on predicted lemming position: ({screen_x}, {screen_y}).")
    else:
        print("No lemmings detected.")

# Use this function instead of test_click_digger_on_lemming
predictive_click_lemming(lemmings, region)