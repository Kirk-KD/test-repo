
from random import choice  # import choice function from random

word = choice(["code", "club"])  # pick a random word from list
chance = len(word) + 5  # give player word length + 5 chances
guessed = []  # define guessed and wrong to check if letter was guessed
wrong = []

while True:  # loop until win or lose
    out = ""

    if chance == 0:  # lose if chance == 0
        print(f"you didn't guess {word}")
        break

    for letter in word:  # replace guessed letters with _
        if letter in guessed:
            out += letter
        else:
            out += "_"

    if out == word:  # win if guessed the word
        print(f"you guessed {word}")
        break

    print(out)  # show word and chances
    print(f"{chance} chances left")

    guess = input("Guess a letter: ")  # get letter

    if guess in guessed or guess in wrong:  # if letter was guessed
        print(f"already guessed {guess}")
        chance -= 1
    elif guess in word:  # if letter is in word
        guessed.append(guess)
        print("yay")
    else:  # if letter is not in word
        wrong.append(guess)
        print("nope")
        chance -= 1

    print()  # empty line
