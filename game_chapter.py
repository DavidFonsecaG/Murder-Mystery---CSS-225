import time


class Chapter:
    def __init__(self, game_state):
        self.game_state = game_state

    def display_scene(self):
        print(self.game_state.data[f'chapter{self.game_state.chapter}']["scene"])

    def display_options(self):
        options = self.game_state.data[f'chapter{self.game_state.chapter}']["actions"]
        print("\nWhat would you like to do:")
        counter = 1
        for option in options:
            print(f'{counter}. {option}')
            counter += 1
        print(f'{counter}. Quit')

    def find_clue(self, action):
        raise NotImplementedError("Subclasses must implement process_choice")

    def process_choice(self, choice):
        raise NotImplementedError("Subclasses must implement process_choice")


class GameChapter(Chapter):

    def __init__(self, game_state, chapter_number):
        super().__init__(game_state)
        self.chapter_number = chapter_number
        self.chapter_data = self.game_state.data[f'chapter{self.chapter_number}']

    def find_clue(self, action):
        action_description = self.chapter_data['actions'][action - 1].lower()
        print(f"\nYou {action_description}. Searching for clues...")

        if action == 2:  # Clue is always found in action 2
            if 'clues' in self.chapter_data and len(self.chapter_data['clues']) > 0:
                clue = self.chapter_data['clues'][0]
                self.game_state.add_clue(clue)
                print(f"You found a clue: {clue}")

        if action == 1:  # Weapon is always found in action 1
            if self.game_state.has_clue(self.chapter_data['clues'][0]):
                self.game_state.weapon_found = self.find_weapon()
            else:
                print("Nothing interesting here. \nYou might need to find something else first.")

        if action == 3:  # Action 3 can be completed only if the weapon is found
            if self.game_state.weapon_found:
                self.game_state.action_completed = True
                print(f"You successfully completed scene {self.game_state.chapter}.")
                if self.chapter_number < len(self.chapter_data):
                    self.game_state.next_chapter()
            else:
                print("You need a specific item to proceed.")

        # Additional logic for Chapter 4 to solve the game
        if self.chapter_number == 4:
            if action == 3:  # Final action to solve the game
                if self.game_state.weapon_found and self.game_state.has_clue(self.chapter_data['clues'][0]):
                    print("With the evidence and resources at hand, you confront the mastermind behind the conspiracy.")
                    print("You successfully solve the case and bring justice to the town.")
                    self.game_state.game_solved = True  # Flag to indicate the game is solved
                else:
                    print("You don't have enough evidence and resources to solve the case yet.")

        time.sleep(2)

    def find_weapon(self):
        if 'weapons' in self.chapter_data and len(self.chapter_data['weapons']) > 0:
            weapon_data = self.chapter_data['weapons'][0]
            player_input = input(weapon_data['question'])
            if player_input.lower() == 'y':
                weapon = weapon_data['type']
                self.game_state.add_weapon(weapon)
                print(f"You found a: {weapon}")
                time.sleep(2)
                return True
            else:
                print("You decided not to use the item.")
                time.sleep(2)
        return False

    def process_choice(self, player_choice):
        player_choice = int(player_choice)
        if player_choice in range(1, len(self.chapter_data['actions']) + 1):
            self.find_clue(player_choice)
        elif player_choice == len(self.chapter_data['actions']) + 1:
            print("\nGoodbye!")
            return True
        else:
            print("Invalid choice. Try again.")
        return False

