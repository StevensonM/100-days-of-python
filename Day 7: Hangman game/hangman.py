# Step 1
from hangman_art import logo
import random

from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')
# Remeber to take this out.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print("Guess a letter in the word.")
    guess = input().lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose :(")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    from hangman_art import stages
    print(stages[lives])
