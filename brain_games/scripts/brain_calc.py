#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import calc_game


def main():
    start_game(calc_game)


if __name__ == '__main__':
    main()
