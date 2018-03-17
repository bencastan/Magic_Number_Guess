from random import randint


def magicnumber_guesser():
    answer = False
    while not answer:
        magic_number = randint(0, 10)
        print("Guess a number between 1 - 10 ")
        guess_number = int(input(">:"))
        if magic_number == guess_number:
            print("Well done you guessed the same number as me!")
            answer = True
        else:
            print("Try again that is not the right number")


magicnumber_guesser()
