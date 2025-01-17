import random
names_string = input("Give me everybody's name, separated by a comma.")
names = names_string.split(',')
names_length = len(names)

random_choice = random.randint(0,names_length -1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + ""+"Is going to pay for the meals today!.")



