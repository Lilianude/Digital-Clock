# First game, the computer has a number and I am guessing the number
import random

def guess(x):
    random_number = random.randint(5,x)
    guess = 0
    while guess != random_number :
        guess = int(input(f'Enter your guess between 5 and {x}: '))
        if guess > random_number:
            print("guess is too high, guess again.") 
        elif guess < random_number:
            print('guess is too low, guess again.')
    print(f"Congrats you have guessed the number {random_number} correctly. ")
      
guess(20)


# Second game, I have a number in mind and I want the computer to guess the number
import random 


def computer_guess(x):
    low = 5
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high :
            guess = random.randint(low,high)
        else:
            guess = low # could also be low
        feedback = input(f'Is {guess} either H for high or L for low or c for correct ??: ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print (f'The computer guessed your correct number {guess}')
    
    
computer_guess(20)