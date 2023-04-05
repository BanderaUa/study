# required homework

# This function takes two numbers and return the biggest.
def the_biggest_number(a, b):
    if a > b:
        return a

    elif a == b:
        return "a and b are equal"

    else:
        return b


# This function takes three numbers and return the smallest

# My first Version

def the_smallest_number(a, b, c):
    if a == b == c:
        return "a and b and c are equal"

    elif a == b < c:
        print(a, "and", b, "are equal and smaller than", c)
        return a and b

    elif a == c < b:
        print(a, "and", c, "are equal and smaller than", b)
        return a and c

    elif b == c < a:
        print(b, "and", c, "are equal and smaller than", a)
        return b and c

    elif b > a < c:
        return a

    elif a > b < c:
        return b

    else:
        return c


# My second version

def the_smallest_number_2(a, b, c):
    if a == b == c:
        return "a and b and c are equal"

    elif a == b < c:
        return a and b

    elif a == c < b:
        return a and c

    elif b == c < a:
        return b and c

    elif b > a < c:
        return a

    elif a > b < c:
        return b

    else:
        return c


# This function takes number and returns his absolute value
def the_absolute_value_of_a_number(a):
    if a < 0:
        return a * (-1)
    else:
        return a


# This function takes two numbers and summ their

def sum_function(a=0, b=0):
    print(a + b)


# This function determines the sign of a number

def sign_detector(a):
    if a > 0:
        print("The number is positive")
    elif a == 0:
        print("This is a zero,it don`t have sign")
    else:
        print("The number is negative")
