def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("NRS", "CRS")
print_two_again("NRS", "CRS")
print_one("First!")
print_none()


def print_one(arg1):
    print(f"arg1: {arg1}")

y = "Firstttt!"
x = "Second!"
print_one(x) # cant have x and y as function takes only one argument