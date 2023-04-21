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

def func_dict_from_x(x):
    return {letter: x.count(letter) for letter in x}


def get_max_str(listed_strings, no_letters=''):
    if not listed_strings:
        return no_letters

    max_str = listed_strings[0]

    for x in listed_strings:
        if len(x) > len(max_str):
            max_str = x

    return max_str


print(get_max_str(['alice','bob','felixlll','johny']))



def make_the_string(a,sign):
    result = sign.join(a)
    return result

print(make_the_string(a = "abc",sign="|"))
