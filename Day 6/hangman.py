import random

# step one
word_list = ["python", "java", "javascript", "csharp"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-4 create an empty list called display
# for each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was 'apple', display should be ['_', '_', '_', '_', '_']
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# TODO-5 loop through each position in the chosen_word
# if the letter at that position matches the guess, update the display list.
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TODO-6 print 'display' and you should see the guessed letter in the correct position
print(display)

# use a while loop to let the user guess again until word is fully revealed
while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

print("You've won!")
