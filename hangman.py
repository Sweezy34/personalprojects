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
