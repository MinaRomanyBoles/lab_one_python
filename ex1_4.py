#Exercise 1.4: Number Guessing Game

import random 

def  guessing_game():
    number_to_guess = random.randint(1, 100)
    print(f'🔎 {number_to_guess} ')
    attempts = 0
    max_attempts = 7
    guess_num = int(input("Guess a number between 1 and 100: "))
    while attempts < max_attempts:
        if guess_num != number_to_guess:
            attempts += 1
            if guess_num < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            if attempts < max_attempts:
                guess_num = int(input(f"Attempt {attempts}/{max_attempts}. Try again: "))
        else:
            print(f"Congratulations! Your guess {guess_num} is correct ")
            return
    print(f"Sorry, you used all {max_attempts} attempts")

while True:
    guessing_game()
    if input("Play again? (yes/no):").lower() == 'yes':
        continue
    else:
        break
