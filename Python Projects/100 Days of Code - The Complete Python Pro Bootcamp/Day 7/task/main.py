word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random

def chosen_word():
   return random.choice(word_list)

finalChosenWord = chosen_word()
print (finalChosenWord)

guessLetter = input("Guess a letter: ").lower()

if guessLetter in chosen_word():
    print("Right")
else:
    print("Wrong")

hiddenWord = ["_"] * len(finalChosenWord)
hiddenWord = "".join(hiddenWord)

print(finalChosenWord)
print(hiddenWord)