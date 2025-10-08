import random

def number_guess():
    number_prediction = random.randint(1, 100)

    attempt = 0
    max_attempt = 7

    print("welcome to the number guessing game!")
    print("i have choosen a number in between 1 to 100:")
    print(f"you have {max_attempt} attempt to guess it.")


    while attempt < max_attempt:
        guess = int(input(f"attempt{attempt +1 }: enter your guess:"))
        attempt += 1

        if guess < number_prediction:
            print("to low ! try again")
        elif guess > number_prediction:
            print("to heigh ! try again")
        else:
            print(f"congratulation you guess the number {number_prediction} correctly in {attempt} attempt!")
            break
    else:
        print(f"sorry you lose all the attempt{max_attempt} , the correct number is {number_prediction}.")

number_guess()