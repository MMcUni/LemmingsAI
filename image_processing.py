import cv2
import os
import numpy as np

def load_templates(images_folder):
    """Load lemming and goal templates from the images folder."""
    lemming_templates = []
    for i in range(1, 17):  # Assuming there are 16 frames numbered from 01 to 16
        template_path = os.path.join(images_folder, f'lemming_template{i:02d}.png')
        lemming_template = cv2.imread(template_path, 0)  # Ensure the template is in grayscale
        lemming_templates.append(lemming_template)
    
    # Load the goal template
    goal_template_path = os.path.join(images_folder, 'goal_template.png')
    goal_template = cv2.imread(goal_template_path, 0)  # Ensure the template is in grayscale

    return lemming_templates, goal_template

def detect_lemmings_and_goal(gray_frame, lemming_templates, goal_template, lemming_threshold=0.8, goal_threshold=0.8):
    """Detect lemmings and the goal in the game screen."""
    lemmings = []  # List to store lemmings' positions
    frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for drawing rectangles

    # Detect lemmings
    for lemming_template in lemming_templates:
        lemming_result = cv2.matchTemplate(gray_frame, lemming_template, cv2.TM_CCOEFF_NORMED)
        lemming_loc = np.where(lemming_result >= lemming_threshold)

        for pt in zip(*lemming_loc[::-1]):  # Switch columns and rows
            lemmings.append(pt)
            cv2.rectangle(frame, pt, (pt[0] + lemming_template.shape[1], pt[1] + lemming_template.shape[0]), (0, 255, 0), 2)

    # Detect goal
    goal_result = cv2.matchTemplate(gray_frame, goal_template, cv2.TM_CCOEFF_NORMED)
    goal_loc = np.where(goal_result >= goal_threshold)
    goal = None

    for pt in zip(*goal_loc[::-1]):  # Switch columns and rows
        goal = pt  # Assume one goal; overwrite previous if detected multiple times
        cv2.rectangle(frame, pt, (pt[0] + goal_template.shape[1], pt[1] + goal_template.shape[0]), (255, 0, 0), 2)

    return lemmings, goal, frame
