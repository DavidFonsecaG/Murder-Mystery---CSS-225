class GameState:
    def __init__(self, game_data):
        self.data = game_data
        self.chapter = 1
        self.weapon_found = False
        self.interaction_completed = False
        self.action_completed = False
        self.inventory = {"weapons": [], "clues": []}
        self.game_solved = False

    def add_weapon(self, weapon):
        self.inventory["weapons"].append(weapon)

    def add_clue(self, clue):
        self.inventory["clues"].append(clue)

    def has_weapon(self, weapon):
        return weapon in self.inventory["weapons"]

    def has_clue(self, clue):
        return clue in self.inventory["clues"]

    def next_chapter(self):
        if self.action_completed:
            self.chapter += 1
            self.reset_chapter_state()

    def reset_chapter_state(self):
        self.weapon_found = False
        self.interaction_completed = False
        self.action_completed = False
