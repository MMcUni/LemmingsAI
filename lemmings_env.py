import cv2
import numpy as np
import pyautogui
from collections import namedtuple
from image_processing import detect_lemmings_and_goal
from actions import click_action, button_coords

Action = namedtuple('Action', ['skill', 'lemming_index'])

class LemmingsEnv:
    def __init__(self, region, lemming_templates, goal_template):
        self.region = region
        self.lemming_templates = lemming_templates
        self.goal_template = goal_template
        self.reset()

    def reset(self):
        self.frame = self.capture_game_state()
        self.lemmings, self.goal = self.process_frame(self.frame)
        self.time_step = 0
        self.lemmings_saved = 0
        return self._get_state()

    def capture_game_state(self):
        screenshot = pyautogui.screenshot(region=self.region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame

    def process_frame(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        lemmings, goal, _ = detect_lemmings_and_goal(gray_frame, self.lemming_templates, self.goal_template)
        return lemmings, goal

    def step(self, action):
        if action.skill != 'wait':
            click_action(action.skill, self.lemmings[action.lemming_index], self.region)
        
        self.time_step += 1
        self.frame = self.capture_game_state()
        self.lemmings, self.goal = self.process_frame(self.frame)
        
        reward = self._calculate_reward()
        done = self._is_done()
        
        return self._get_state(), reward, done, {}

    def _get_state(self):
        # Create a simplified state representation
        state = np.zeros((50, 50), dtype=np.int8)  # Adjust size as needed
        for lemming in self.lemmings:
            x, y = lemming
            state[y//10, x//10] = 1  # Simplify coordinates
        if self.goal:
            state[self.goal[1]//10, self.goal[0]//10] = 2
        return state

    def _calculate_reward(self):
        reward = 0
        current_lemmings = len(self.lemmings)
        saved = current_lemmings - self.lemmings_saved
        if saved > 0:
            reward += saved * 10
        self.lemmings_saved = current_lemmings
        reward -= 0.1  # Small penalty for each time step
        return reward

    def _is_done(self):
        return len(self.lemmings) == 0 or self.time_step >= 1000  # Adjust max steps as needed

    def get_action_space(self):
        return [Action(skill, i) for skill in button_coords.keys() for i in range(len(self.lemmings))] + [Action('wait', 0)]