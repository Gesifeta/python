import random
word_list = ["aardvark", "baboon", "camel"]


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessed_word=""
for char in chosen_word:
    guessed_word +='-'

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
counter = len(chosen_word)
while counter >0:
    guess = input("Guess a letter: ").lower()
    print("=========")
    print(f"****************************{counter}/{len(chosen_word)} LIVES LEFT****************************")
    if  chosen_word.lower().find(guess.lower()) != -1:
        for num in range(0,len(guessed_word)):
            if num == chosen_word.lower().find(guess.lower()):
                chosen_word.replace("a", guess)
                print("guess==>",chosen_word)
    else:
        print(f"Sorry, the letter '{guess.lower()}' is not in the word! {chosen_word.lower()} is not in the word.")
        counter -= 1
    print("Word to guess: ",guessed_word)
    print("=========")
