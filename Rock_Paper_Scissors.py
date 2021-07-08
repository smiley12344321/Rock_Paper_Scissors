import random


print("Welcome to Rock Paper Scissors ")

start =0
welcome = int(input("If you already know how to play, type 1. If you want to know more about the game and the rules, type 2 "))
if welcome == 1:
    start = 1
if welcome == 2:
    print("Rock Paper Scissors is a game played by many people around the world.")
    print("It is played by 2 people and they both choose either rock, paper, or scissors")
    print("Paper beats Rock, Rock beats Scissors, and Scissors beat Paper.")
    starting = int(input("Once you are ready to play type 1"))
    if starting == 1:
        start=1

if start == 1:
    botq = int(input("Enter 1 for bot and 2 for 2 player: "))
    if botq == 1:
        name = str(input("Enter your name: "))
    if botq == 2:
        name1 = str(input("Enter player 1 name: "))
        name2 = str(input("Enter player 2 name: "))

    x = 100

    if botq == 2:
        player1in = int(input("Enter 1 for rock 2 for siccors and 3 for paper: "))
        player2in = int(input("Enter 1 for rock 2 for siccors and 3 for paper: "))

        if player1in == 1 and player2in == 2:
            print(name1, "win")
        if player1in == 2 and player2in == 3:
            print(name1, "win")
        if player1in == 3 and player2in == 1:
            print(name1, "win")
        if player1in == 2 and player2in == 1:
            print(name2, "win")
        if player1in == 3 and player2in == 2:
            print(name2, "win")
        if player1in == 1 and player2in == 3:
            print(name2, "win")
        elif player1in == player2in:
            print("Tie")
    if botq == 1:
        player1botin = int(input("Enter 1 for rock 2 for siccors and 3 for paper: "))
        n = random.randint(1, 3)
        if player1botin == 1 and n == 2:
            print(name, "win")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        elif player1botin == 2 and n == 3:
            print(name, "win")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        elif player1botin == 3 and n == 1:
            print(name, "win")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        elif player1botin == 2 and n == 1:
            print("Bot Won")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        elif player1botin == 3 and n == 2:
            print("Bot won")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        elif player1botin == 1 and n == 3:
            print("Bot won")
            print("Bot chose: ", n)
            print("1 = rock, 2 = siccors, 3 = paper")
        else:
            print("Tie")

