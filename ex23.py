fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadilliac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizzare']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

print(fruit [0][1])
print(fruit [0][2])
print(fruit [2][1])
print(fruit [1][0])
print(fruit [3][0])
print(fruit [3][1])
print(fruit [0][0])

print(cars [0][1][1])
print(cars [1][1][0])
print(cars [2][1][2])
print(cars [3][1][0])
print(cars [3][1][2])
print(cars [0][1][0])
print(cars [0][1][2])
print(cars [2][1][0])

print(languages [0][1][0])
print(languages [1][1][1][0])
print(languages [3][1][1][1])
print(languages [4][1][0])
print(languages [4][1][1][1])
print(languages [4][1][1][0])
print(languages [3][1][1][0])
print(languages [2][1][1][1])
print(languages [1][1][0])

print(cars[1][1][1])
print(cars[1][1][0])
print(cars[1][0])
print(cars[3][1][1])
print(fruit[3][2])
print(languages[0][1][1][1])
print(fruit[2][1])
print(languages[3][1][0])