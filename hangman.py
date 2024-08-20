import random

def hangman():
    words = ["police" , "boots" , "taser" , "computer ", "america"]
    print(words)
   
    chosen_word = random.choice(words)
    print(chosen_word)
   
    num_guesses = len(chosen_word)
    print(num_guesses)
   
    word_list = list(chosen_word)
    print(word_list)
   
    display_word = ""

    for i in range(len(chosen_word)):
        display_word += "-"

    display_list = list(display_word)
    print(f"this is the display: \n{display_list}")
   
    while num_guesses > 0 and len(word_list) > 0:
       
        guess = input("Pick a letter ")
           
        if guess in word_list:
            display_list[word_list.index(guess)] = guess
            word_list[word_list.index(guess)] = "-"
            print(f"index is {word_list.index(guess)}")
            print("Guess is right")
            print(f"This is the display: \n{display_list}")
            print(word_list)
        else:
            num_guesses -= 1
            print("Guess is wrong")
            print(num_guesses)
           
    if num_guesses == 0:
        print("You suck and you lose")
    elif not word_list:
        print("You win")

   
hangman()

#This is my best attempt at hangman without trying to follow along with the lesson and doing it completely on my own. The idea is to pick a random word from the first list and then create another list with the same length full of underscores.
#It was supposed to work by swapping the correct letter with the dashes in the same index, but I couldn't quite get it to work. I went to bed yesterday frustrated and a little behind on the class.
#Going to try and follow along with the professor now, still, I gave it the old-fashoned try.


#Below is my final solution (insert bad hitler joke here) to the hangman() problem. I had to follow along some parts of this with the professor, but I kinda get it... sort of.
#Still not entirely solid on how the program knows what to index where, but I think if I sat down with it and really took a look I'd get it better.
#At this point i'm sick of this program and I'm happy to kiss it goodbye... i hate hangman! >:( good riddance!!!

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]


lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
        break

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print("Game Over")
        print(stages[lives])
        break

    print(stages[lives])

#looking back, I think I should have made the ascii art in this a separate library and then just import it, just to make it all look cleaner. Like I said above though, I'm done with this haha


*************************************************************************************
#Just for giggles, I asked ChatGPT to see if it could help correct my original code, this is what it gave me:

import random

def hangman():
    # List of possible words for the game
    words = ["police", "boots", "taser", "computer", "america"]
    
    # Randomly select a word from the list
    chosen_word = random.choice(words)
    word_list = list(chosen_word)  # Convert the word to a list of characters
    display_list = ["-" for _ in chosen_word]  # Create a list to show progress in guessing
    
    num_guesses = 6  # Set a reasonable number of guesses for the player
    guessed_letters = set()  # To keep track of guessed letters
    
    # Main game loop
    while num_guesses > 0 and "-" in display_list:
        # Display current state of the word, number of guesses left, and guessed letters
        print(f"Current word: {' '.join(display_list)}")
        print(f"Guesses left: {num_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Get user input and convert to lowercase
        guess = input("Pick a letter: ").lower()
        
        # Validate input: must be a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)  # Add the guessed letter to the set
        
        # Check if the guessed letter is in the word
        if guess in word_list:
            print("Guess is right!")
            # Update the display_list with all occurrences of the guessed letter
            for i, letter in enumerate(word_list):
                if letter == guess:
                    display_list[i] = guess
        else:
            # Incorrect guess; decrement the number of guesses left
            num_guesses -= 1
            print("Guess is wrong.")
        
        print()
    
    # Check if the game is won or lost
    if "-" not in display_list:
        print(f"Congratulations! You've guessed the word: {''.join(display_list)}")
    else:
        print(f"Sorry, you've run out of guesses. The word was: {chosen_word}")

hangman()


#It also explained the changes in comments below.... isn't technology amazing?!!
