import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose something from the list
    while '-' in words or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word list, to ensure no duplicates
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guessed
    
    lives = 6
    
# getting user input

    while len(word_letters) > 0  and lives > 0:
        # displays used letters
        #''.join(['a', 'b', 'cd']) => 'a b cd'
        print('You have', lives, 'left and you have used these letters: ', ' '. join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        
        user_letter = input ('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters: #if the user unpit is a valid alphabet that has not been used yet.
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) # essentialy if you guess th letter right, it removes the letter from the word you are meant to guess.
            
            else:
                lives = lives - 1 # takes away one life
                print ('Letter is not in word')
                
    
        elif user_letter in used_letters: # if you have already guessed that letter do the next line.
            print('You have already used that character, Please try again.')
            
        else :
            print ('Invalid Character, try again.') # program gets here when the len(words) == 0 and when lives == 0
        
        
    if lives == 0:
        print('Sorry you have died, the correct word was', word)
        
    else :
        print('You guessed the word correctly', word, '!!')
        
            
hangman()
        