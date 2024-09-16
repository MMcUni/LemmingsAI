from memory_reader import LemmingsMemoryReader
from memory_actions import LemmingsMemoryActions
from lemmings_dqn import DQNAgent
import numpy as np
import time

def calculate_reward(state):
    # This is a placeholder reward function. Adjust based on your game understanding.
    saved_lemmings = state.get(hex(0x461364), 0)  # Assuming this address holds the number of saved lemmings
    total_lemmings = state.get(hex(0x461360), 100)  # Assuming this address holds the total number of lemmings
    return saved_lemmings / total_lemmings

def is_done(state):
    # This is a placeholder done condition. Adjust as needed.
    total_lemmings = state.get(hex(0x461360), 100)  # Assuming this address holds the total number of lemmings
    saved_lemmings = state.get(hex(0x461364), 0)  # Assuming this address holds the number of saved lemmings
    lost_lemmings = state.get(hex(0x461368), 0)  # Assuming this address holds the number of lost lemmings
    return (saved_lemmings + lost_lemmings) >= total_lemmings

def main():
    reader = LemmingsMemoryReader()
    actions = LemmingsMemoryActions()

    state_shape = (len(reader.important_addresses),)
    n_actions = len(actions.skills) * actions.get_lemming_count()

    agent = DQNAgent(state_shape, n_actions)

    n_episodes = 1000
    for episode in range(n_episodes):
        state = actions.get_game_state()
        state_list = list(state.values())
        total_reward = 0
        done = False
        
        while not done:
            action = agent.act(state_list)
            
            # Convert action to skill and lemming index
            skill_index = action // actions.get_lemming_count()
            lemming_index = action % actions.get_lemming_count()
            skill = actions.skills[skill_index]
            
            # Apply the action
            actions.apply_skill(skill, lemming_index)
            
            # Wait a bit for the game to react
            time.sleep(0.1)
            
            next_state = actions.get_game_state()
            next_state_list = list(next_state.values())
            
            reward = calculate_reward(next_state)
            done = is_done(next_state)
            
            agent.remember(state_list, action, reward, next_state_list, done)
            agent.replay()
            
            state = next_state
            state_list = next_state_list
            total_reward += reward
        
        if episode % 10 == 0:
            agent.update_target_model()
        
        print(f"Episode: {episode}, Total Reward: {total_reward:.2f}, Epsilon: {agent.epsilon:.2f}")

if __name__ == "__main__":
    main()