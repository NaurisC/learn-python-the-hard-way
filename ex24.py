fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
];

cars = [
    {'type': 'Cadilliac', 'color': 'Black',
     'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red',
     'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue',
     'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White',
     'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow',
     'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate',
     'opinion': ['Alright', 'Bizzare']},
    {'name': 'Perl6', 'speed': 'Moderate',
     'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast',
     'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast',
     'opinion': ['Fun', 'Difficult']}   
];

print(fruit[0]['count'])
print(fruit[0]['rating'])
print(fruit[2]['count'])
print(fruit[1]['kind'])
print(fruit[3]['kind'])
print(fruit[3]['count'])
print(fruit[0]['kind'])

print('////////////////////////////')

print(cars[0]['size'])
print(cars[1]['color'])
print(cars[2]['miles'])
print(cars[3]['color'])
print(cars[3]['miles'])
print(cars[0]['color'])
print(cars[0]['miles'])
print(cars[2]['color'])

print('////////////////////////////')

print(languages[0]['speed'])
print(languages[1]['opinion'][0])
print(languages[3]['opinion'][1])
print(languages[3]['speed'])
print(languages[4]['opinion'][1])
print(languages[2]['opinion'][0])
print(languages[3]['opinion'][0])
print(languages[2]['opinion'][1])
print(languages[2]['speed'])

print('////////////////////////////')

print(cars[1]['size'])
print(cars[1]['color'])
print(cars[1]['type'])
print(cars[3]['size'])
print(fruit[3]['rating'])
print(languages[0]['opinion'][1])
print(fruit[2]['count'])
print(languages[3]['speed'])