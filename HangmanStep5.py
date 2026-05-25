# Step 5.
import random
# Delete Word_list.
#
from Hangman_words import word_list

choosen_word = random.choice(word_list)
word_length = len(choosen_word)

end_of_game = False
lives = 6

# Import Logo.
from Hangman_art import (logo, stages)
print(logo)

# Testing Code.
#print(f"The Solution is {choosen_word}")

# Create Blanks.
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
     print(f"You've already guessed {guess}")

# Check Guess Letter.
    for position in range(word_length):
        letter = choosen_word[position]
        print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {guess}")
        if letter == guess:
          display[position] = letter

# Check if user is wrong.
    if guess not in choosen_word:
     print(f"You guessed  {guess}, that's not in the word. You lose a Life.")
     lives -= 1
     if lives == 0:
        end_of_game = True
        print("You Lose.")

# Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

# Check if user has got all letters.
    if "_" not in display:
      end_of_game = True
      print("You Win.")

# Import the Stages.
# Print(stages[lives])
