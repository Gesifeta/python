import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
if  chosen_word.lower().find(guess.lower()) != -1:
    print(f"You guessed the letter '{chosen_word.lower()}' correctly!")
else:
    print(f"Sorry, the letter '{guess.lower()}' is not in the word! {chosen_word.lower()} is not in the word.")

print(chosen_word.lower().find(guess.lower()))