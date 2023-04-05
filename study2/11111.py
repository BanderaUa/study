# def the_biggest_number(a,b):
#     if a > b:
#         return a
#     elif a == b:
#         return "a and b are equal"
#     else:
#         return b


def the_smallest_number(a,b,c):
    if a == b == c:
        print( "a and b and c are equal")
    elif b>a<c:
        print(a)
    elif a>b<c:
        print(b)
    else:
         print(c)

e = (the_smallest_number(1,6,2))
x = (the_smallest_number(6,3,1))


c = (10 * e * x)
print(c)