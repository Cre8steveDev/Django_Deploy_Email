# Create a function that takes two numbers start and end. The function should then print nubers divisible by 2 between the start and end numbers provided.


def print_num(start, end):
    for x in range(start, end + 1):
        if x % 2 == 0:
            print(x)


print_num(10, 18)
print_num(30, 40)
