def rule_based_ai(lemmings, goal):
    """Simple rule-based AI logic to decide actions."""
    actions = []
    for lemming in lemmings:
        x, y = lemming
        
        # Example rules:
        if y < 100:  # Close to the top of the screen (adjust based on game logic)
            actions.append(("builder", (x, y)))
        elif x < 100:  # Close to the left edge (adjust based on game logic)
            actions.append(("climber", (x, y)))
        elif close_to_trap(x, y):  # Example function to detect proximity to a trap (needs implementation)
            actions.append(("blocker", (x, y)))
        else:
            actions.append(("walker", (x, y)))  # Default action

    return actions

def close_to_trap(x, y):
    """Placeholder function to check if a lemming is close to a trap. Needs implementation."""
    # Implement actual logic to detect traps based on game state
    return False
