import random
from typing import Dict, List
from game_objects import Player, Roll

SCISSOR = "Scissor"
ROCK = "Rock"
PAPER = "Paper"

def build_the_rolls():
    return {
        ROCK: Roll(ROCK, defeating=[SCISSOR], defeated_by=[PAPER]),
        SCISSOR: Roll(SCISSOR, defeating=[PAPER], defeated_by=[ROCK]),
        PAPER: Roll(PAPER, defeating=[ROCK], defeated_by=[SCISSOR])
    }

def main():
    print_header()

    rolls = build_the_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def game_loop(player1: Player, player2: Player, rolls):
    count = 1
    while count < 4:
        p2_roll = random.choice(list(rolls.values())) # TODO: get random roll
        roll = input("Which roll? [R]ock, [S]cissor or [P]aper \n")
        roll = {"R": ROCK, "S": SCISSOR, "P": PAPER}[roll]
        p1_roll = rolls[roll] # TODO: have player choose a roll
        outcome = p1_roll.can_defeat(p2_roll)

        print(f"Computer chose {p2_roll.name}")
        print(f"Player chose {p1_roll.name}")

        if outcome == 'WON':             # player one Won
            print(f"Player wins round {count}")
            player1.wins += 1
        elif outcome == 'LOSE':
            print(f"Computer wins round {count}")
            player2.wins += 1
        elif outcome == 'TIE':
            print(f"That was a TIE")

        count += 1

    if player1.wins >= player2.wins:
        print(f"Player wins {player1.wins} : {player2.wins}")
    else:
        print(f"Computer wins {player1.wins} : {player2.wins}")


def print_header():
    print('---------------------------------')
    print('     Rock, Paper, Scissors')
    print('---------------------------------')
    print()

def get_players_name():
    print("Hello you unworthy filth")
    name = input("Which name do you go by?\n")
    return name

if __name__ == '__main__':
    main()
