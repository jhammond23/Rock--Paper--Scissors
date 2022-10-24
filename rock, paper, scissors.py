from operator import index
import random
import time
import string

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(prompt, x=2):
    time.sleep(x)
    print(prompt)


def valid_input(prompt, options):
    while True:
        time.sleep(3)
        with_punc = input(prompt).lower()
        option = with_punc.translate(str.maketrans('', '', string.punctuation))
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try agian! \n')


class Player:
    my_move = None
    their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = valid_input('Would you like to chose "rock", "paper", or '
                           '"scissors"? \n\n', moves)
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_wins = 0
        self.p2_wins = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"\nPlayer 1: {move1}  Player 2: {move2} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            print_pause('   ***Player ONE wins this round!*** \n', 3)
            self.p1_wins += 1
        elif beats(move2, move1) is True:
            print_pause('   ***Player TWO wins this round!*** \n', 3)
            self.p2_wins += 1
        elif move1 == move2:
            print_pause('   ***It looks like this round is a TIE!*** \n', 3)
        else:
            print_pause('Please choose "rock", "paper", or "scissors". \n\n')

    def winner(self):
        if self.p1_wins == 3:
            print_pause('   *****CONGRATULATIONS! Player ONE wins!!!***** \n')
            print_pause(f'Player ONE ends with {self.p1_wins} and Player TWO'
                        f' ends with {self.p2_wins}!')
        elif self.p2_wins == 3:
            print_pause('   *****CONGRATULATIONS! Player TWO wins!!!*****')

    def play_game(self):
        print_pause("Game start!", 2)
        while True:
            for round in range(1, 99):
                self.winner()
                if self.p1_wins == 3:
                    break
                elif self.p2_wins == 3:
                    break
                print_pause(f"Round {round}:", 1)
                self.play_round()
                print_pause(f"Player ONE has {self.p1_wins} points and "
                            f"Player TWO has {self.p2_wins} points. \n\n", 4)
            print_pause("Game over!")
            break


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
