Your goal is to build a Hangman game using everything you have learnt about Python programming.

Demo Final Project
https://appbrewery.github.io/python-day7-demo/

The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each todo in order and complete them.

You can view all the todos easily in PyCharm by going to View -> Tool Windows -> TODOs

TODO-1
Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

TODO-2
Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.


Search Google for the lower() function in Python.
TODO-3
Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.

 Hint 2 
You can loop through Strings the same way you can loop through Lists - by using the `for in` loop. Try Googling: "Loop through strings python"


TODO-2
Create an empty string called "display".
Loop through each letter in the chosen_word
If the letter at that position matches guess then reveal that letter in the display at that position.
e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
Print display and you should see the guessed letter in the correct position.
But every letter that is not a match is represented with a "_".

TODO-1
Use a while loop to let the user guess again.
The loop should only stop once the user has guessed all the letters in the chosen_word.
At that point display has no more blanks ("_"). Then you can tell the user they've won.

TODO-2
Update the for loop so that previous guesses are added to the display String.
At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.

TODO-1:
Create a variable called lives to keep track of the number of lives left.
Set lives to equal 6.
TODO-2:
If guess is not a letter in the chosen_word, Then reduce lives by 1.
If lives goes down to 0 then the game should end, and it should print "You lose."
 Hint 
TODO-3:
print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.

TODO-1:
Update the word list to use the word_list from hangman_words.py
TODO-2:
Update the code to use the stages from the file hangman_art.py
TODO-3:
Import the logo from hangman_art.py and print it at the start of the game.
TODO-4:
If the user has entered a letter they've already guessed, print the letter and let them know.
We should not deduct a life for this.
e.g. You've already guessed a
TODO-5:
If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
e.g. You guessed d, that's not in the word. You lose a life.
TODO-6:
Update the code below to tell the user how many lives they have left. print("****************************<???>/6 LIVES LEFT****************************")
TODO 7:
Update the print statement to give the user the correct word they were trying to guess.
e.g. IT WAS <Correct Word>! YOU LOSE