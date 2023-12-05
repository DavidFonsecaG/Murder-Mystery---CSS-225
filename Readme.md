# Adventure Game Project

## Overview
Welcome to the **Adventure Game**! This Python-based game takes you through a series of challenges where you make choices that determine the outcome of the game. Each level offers unique scenarios and decisions, making your journey exciting and unpredictable.

## Files Description
1. **`game.py`**: The core file that initiates the game. It handles the main menu and the transitions between different levels of the game.

2. **`game_chapter.py`**: Contains the `Chapter` class, responsible for managing the narrative and choices available in each chapter of the game.

3. **`game_data.json`**: A JSON file that holds the data for the game's chapters, including scenes, actions, clues, and weapons.

4. **`game_state.py`**: Defines the `GameState` class, which tracks the state of the game, including the current chapter, player's inventory, and overall game progress.

5. **`main.py`**: The starting point of the game. It sets the stage for the game's adventure and invokes the main game loop.

6. **`util.py`**: Provides utility functions, such as loading game data from the JSON file.

## How to Play
1. Ensure you have Python installed on your system.
2. Download all the project files and place them in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the directory where the files are located.
5. Run the command `python main.py` to start the game.
6. Follow the on-screen prompts to navigate through the game.

## Game Mechanics
- The game starts at level 1 and progresses through various levels, each offering unique challenges and choices.
- In each level, you will be presented with a scenario and a set of choices.
- Your decisions will affect the outcome of the game and lead you to different paths.
- The game employs a dynamic function call system using `globals()["level_" + str(current_level)]` to move to the appropriate level based on your progress.
- If you succeed in a level, you progress to the next one. If not, you may need to retry.

## Enjoy the Adventure!
Dive into the adventure and see where your choices take you. Each level is a new experience, and your decisions shape the course of your journey. Happy gaming!

---

**Note**: This README is a basic guide to get you started with the game. For more detailed instructions or if you encounter any issues, refer to the comments within each file for further explanations.
