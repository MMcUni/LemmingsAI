from memory_reader import LemmingsMemoryReader

class LemmingsMemoryActions:
    def __init__(self):
        self.reader = LemmingsMemoryReader()
        self.reader.connect()
        self.skills = ['climber', 'floater', 'bomber', 'blocker', 'builder', 'basher', 'miner', 'digger']
        
        # These addresses are placeholders. You'll need to find the correct addresses for each action.
        self.skill_addresses = {
            'climber': 0x4157B0,
            'floater': 0x4157B4,
            'bomber': 0x4157B8,
            'blocker': 0x4157BC,
            'builder': 0x4157C0,
            'basher': 0x4157C4,
            'miner': 0x4157C8,
            'digger': 0x4157CC
        }
        
        # This address is a placeholder for where to write the lemming index
        self.target_lemming_address = 0x4157D0
        
    def apply_skill(self, skill, lemming_index):
        if skill not in self.skills:
            print(f"Invalid skill: {skill}")
            return False
        
        # Write the lemming index to memory
        self.reader.write_memory(self.target_lemming_address, lemming_index)
        
        # Write to the skill address to trigger the action
        self.reader.write_memory(self.skill_addresses[skill], 1)
        
        print(f"Applied {skill} to lemming at index {lemming_index}")
        return True

    def get_game_state(self):
        return self.reader.read_memory()

    def get_lemming_count(self):
        # This address is a placeholder. You'll need to find the correct address.
        return self.reader.read_memory()[hex(0x461360)]

# Usage example
if __name__ == "__main__":
    actions = LemmingsMemoryActions()
    game_state = actions.get_game_state()
    print("Current game state:", game_state)
    
    lemming_count = actions.get_lemming_count()
    print(f"Current lemming count: {lemming_count}")
    
    # Example of applying a skill
    actions.apply_skill('blocker', 0)  # Apply blocker to the first lemming