import random
from hangman_words import word_list
from hangman_art import logo, stages

# randomly choice a word
chosen_word = random.choice(word_list)

end_of_game = False
lives = 6

# print welcome hangman logo
print(logo)

# create and display empty list
display = []
for _ in range(len(chosen_word)):
    display.append("_")

# loop through game
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed the letter. Try another one.")
        
    # guess is correct
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    # guess is incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. Lives remaining: {lives}")
        if lives < 1:
            end_of_game = True
            print(f"You lose.\nThe answer is: {chosen_word}")

    # print updated list
    print(f"{' '.join(display)}")

    # end of game
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print hangman art
    print(stages[lives])