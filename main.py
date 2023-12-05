# Crystal Villa, David Fonseca
# Python game - Murder Mystery
# Project developed for CSS-225 Introduction to Applied Programming

import game
import util as u


def main():
    print("\nWelcome to Murder Mystery!")

    # Game objective
    print("\nYour objective is to solve the mysterious murder of Mayor Richard Thornton.")

    # Get game data from json file
    game_data = u.connect_data()

    # Start Game
    game.start(game_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
