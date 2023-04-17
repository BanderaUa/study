import collections

a = "Homework"
b = a[::-1]
c = len(a)
d = list(a)
n = "|".join(a[::3])


def func_1(x):
    d = list(x)
    s = collections.Counter(d)
    return s



def func_2(*args):
    d = list(args)
    for i in d:
        return


func_2('abc','c','abcd','ab')


def func_3(k,*args):
    x = k.join(args)
    return x

