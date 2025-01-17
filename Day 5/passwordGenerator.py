# a simple program that asks the user to input a number and the program generates a password

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
           'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
           'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

print("Welcome to the password generator")
nr_letters = int(input("How many characters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# we need to make sure that the password has at least one letter, one number and one symbol
password = ""
for letter in range(1,nr_letters+1):
    randomCharacter = random.choice(letters)
    password += randomCharacter

for symbol in range(1,nr_symbols+1):
    randomCharacter = random.choice(symbols)
    password += randomCharacter
for number in range(1,nr_numbers+1):
    randomCharacter = random.choice(numbers)
    password += randomCharacter
print(password) 

password_list = []
for letter in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for symbol in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
for number in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
random_password = ""
for char in password_list:
    random_password += char
print(f"Your password is: {random_password}")
