# reinforcement_learning.py

import random
from collections import defaultdict

class ReinforcementLearningAI:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.q_table = defaultdict(lambda: {action: 0 for action in actions})
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.actions = actions

    def choose_action(self, state):
        if random.random() < self.exploration_rate:
            return random.choice(self.actions)
        else:
            return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward, next_state):
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state].values())
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * next_max_q - current_q)
        self.q_table[state][action] = new_q

def state_to_string(lemmings, goal):
    # Convert the game state to a string representation
    return f"Lemmings:{len(lemmings)},GoalDist:{abs(lemmings[0][0] - goal[0]) if goal else 'Unknown'}"

def get_reward(lemmings, goal, level_complete):
    if level_complete:
        return 100  # High reward for completing the level
    elif not lemmings:
        return -100  # Penalty for losing all lemmings
    elif goal:
        return -abs(lemmings[0][0] - goal[0])  # Negative reward based on distance to goal
    else:
        return -1  # Small negative reward for each step to encourage efficiency

def reinforcement_learning_ai(lemmings, goal, ai, level_complete=False):
    state = state_to_string(lemmings, goal)
    actions = []

    for lemming in lemmings:
        action = ai.choose_action(state)
        actions.append((action, lemming))

    reward = get_reward(lemmings, goal, level_complete)
    next_state = state_to_string(lemmings, goal)  # This should be updated after actions are applied
    
    for action, _ in actions:
        ai.update(state, action, reward, next_state)

    return actions

# Usage in main_game_loop:
# ai = ReinforcementLearningAI(['climber', 'floater', 'exploder', 'blocker', 'builder', 'basher', 'miner', 'digger', 'walker'])
# actions = reinforcement_learning_ai(lemmings, goal, ai, level_complete)