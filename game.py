# Main menu. Function that starts or quits the game.
from game_state import GameState
from game_chapter import GameChapter


def start(game_data):
    game_state = GameState(game_data)

    while True:
        chapter_number = game_state.chapter
        current_chapter = GameChapter(game_state, chapter_number)
        current_chapter.display_options()
        player_choice = input("Choose an option: ")

        if current_chapter.process_choice(player_choice):
            break
        if current_chapter.game_state.game_solved:
            break

