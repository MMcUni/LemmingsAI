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
    # Note: 'walker' is not included as it is the default state
}

def click_action(action, lemming_position, button_coords):
    """Simulate a click on a button and a lemming."""
    try:
        if action != "walker":
            # Click on the action button
            pyautogui.click(button_coords[action])
            time.sleep(0.1)  # Short delay to ensure the game registers the button click
        
        # Click on the lemming
        pyautogui.click(lemming_position)
        print(f"Performed action '{action}' at position {lemming_position}")
    except KeyError:
        print(f"Warning: Action '{action}' is not defined in button_coords. Skipping button click.")
    except Exception as e:
        print(f"Error performing action '{action}': {str(e)}")

def execute_actions(actions, button_coords):
    """Execute actions based on AI decisions."""
    for action, lemming_pos in actions:
        click_action(action, lemming_pos, button_coords)
        time.sleep(0.2)  # Add a short delay between actions to prevent overwhelming the game