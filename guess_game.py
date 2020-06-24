
import random

num = 0
playing = True

def ask_for_difficulty():

    difficulty = input("Type E (easy), M (medium), or H (hard) to choose a difficulty: ")
    global num

    if difficulty == "E":
        num = random.randint(1, 20)
    elif difficulty == "M":
        num = random.randint(1, 50)
    elif difficulty == "H":
        num = random.randint(1, 100)
    else:
        print("Only choose E, M, or H.")
        ask_for_difficulty()

def ask_play_again():
    option = input("Type Y to play again, any other key to exit: ")
    if option != "Y":
        global playing
        playing = False

def ask_for_guess():
    try:
        guess = int(input("Guess a number: "))
    except:
        print("Choose a number.")
        ask_for_guess()

    if guess < num:
        print("too low")
        ask_for_guess()
    elif guess > num:
        print("too high")
        ask_for_guess()
    else:
        print("correct")

while playing:
    ask_for_difficulty()
    ask_for_guess()
    ask_play_again()



# https://www.draw.io/
