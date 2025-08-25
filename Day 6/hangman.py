import random
from stages import stages

# Word bank
word_list = ["python", "java", "javascript", "csharp", "hangman", "developer"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Setup
display = ["_"] * word_length
lives = len(stages) - 1
guessed_letters = set()

print("Welcome to Hangman!")

# Main game loop
while "_" in display and lives > 0:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Validate repeated guesses
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    guessed_letters.add(guess)

    # Check guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives left: {lives}")
        print(stages[lives])

# Outcome
if "_" not in display:
    print("\n" + " ".join(display))
    print("🎉 You've won! The word was:", chosen_word)
else:
    print(stages[0])
    print("💀 You lost! The word was:", chosen_word)
