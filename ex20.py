from sys import argv

input_file = "ex20_test.txt"

def print_all(f):
    print(f.read()) # read the file and print it

def rewind(f):
    f.seek(0) # seek() is used to move the cursor to a particular position in the file. 0 is the beginning of the file. 1 is the first byte of the file, 2 is the second and so on. Basiocally move letter by letter

def print_a_line(line_count, f):
    print(line_count, f.readline()) # read the line and print it. readline() reads a single line from the file and moves the cursor to the next line

current_file = open(input_file) # opent the file and store it in a variable current_file

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 # current_line = 2
print_a_line(current_line, current_file)

# rewind(current_file) here would rewind the file to the beginning of the file. So the next line would print the first line again

current_line += 1 # current_line = 3, += is a shorthand for current_line = current_line + 1
print_a_line(current_line, current_file)

