ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')

try:
    print(f'{person} is {ages[person.capitalize()]} years old.')
except KeyError:
    print(f"{person}'s age is unknown.")