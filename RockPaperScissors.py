# Rock Paper Scissors Game
# Based on the 12 Beginner Python Projects Tutorial from freeCodeCamp.org
# Tutorial by Kylie Ying
# Link to Youtube Tutorial: https://youtu.be/8ext9G7xspg

import random


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

def play():
    user = input("What's your choice? 'r' for rock,'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

print(play())