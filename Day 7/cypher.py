from art import logo
print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26 
            end_text += alphabet[new_position]
        else:
            # Keep non-alphabet characters (spaces, punctuation, numbers)
            end_text += letter

    print(f"The {cipher_direction}d text is: {end_text}")


# User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Normalize shift in case it's larger than 26
shift = shift % 26

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)