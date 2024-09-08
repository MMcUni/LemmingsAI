import pyautogui

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

def click_action(action, lemming_position, button_coords):
    """Simulate a click on a button and a lemming."""
    # Click on the action button
    pyautogui.click(button_coords[action])
    # Click on the lemming
    pyautogui.click(lemming_position)

def execute_actions(actions, button_coords):
    """Execute actions based on AI decisions."""
    for action, lemming_pos in actions:
        click_action(action, lemming_pos, button_coords)
