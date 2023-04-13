# TASK 1

def func_1(*args):
    return list(set(args))


# TASK 2

def func_2(**kwargs):
    if "user_type" not in kwargs:
        kwargs["user_type"] = "Student"
    print(len(kwargs))
    print(kwargs)


func_2(a=4, b=6, c=8, user_type='teacher')


# TASK 4

def func_3(a):
    def func_4(b):
        return a * b

    return func_4


x = func_3(4)
print(x(9))


# TASK 3

def func_5(a, b, /, c, *, d, e=4, f=4):
    return a, b, c, d, e, f

# TASK 5
def printing_square(x):
    if x == 0:
        return 0
    if x >= 1 :
        b ="*" * int(x)
        print(b)

printing_square(2)