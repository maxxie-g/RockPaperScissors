# TODO: include in applet with other games

import random

def play():
    print("Hello traveler and welcome to the wonderful world of RPS!!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play [R]ock, [P]aper, [S]cissors against a machine? Y/N  ".format(player_name))
    humanScore = 0
    machineScore = 0

    while wanna_play.lower() == "y":
        computer = random.choice(['r','p','s'])
        user = input("What's your choice? R/P/S  ")
        print("Machine chose: ",computer)

        if user == computer:
            print("It's a tie!")
            print("The score is: Machine ",str(machineScore)," | ",str(humanScore)," Human")
            play_again = input("Let's try that again, shall we? Y/N  ")
            if play_again.lower() == "n":
                print("That's cool, have a good one!")
                break

        elif is_win(user, computer):
            humanScore += 1
            print("You won!")
            print("The score is: Machine ",str(machineScore)," | ",str(humanScore)," Human")
            play_again = input("Another game to see if it's beginner's luck? Y/N  ")
            if play_again.lower() == "n":
                print("That's cool, have a good one!")
                break
        
        else:
            machineScore += 1
            print("You lost, you loser!")
            print("The score is: Machine ",str(machineScore)," | ",str(humanScore)," Human")
            play_again = input("Anotha one? Y/N  ")
            if play_again.lower() == "n":
                print("That's cool, have a good one!")
                break
    else:
        print("That's cool, have a good one!")

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())