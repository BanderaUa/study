import random


def summ_of_lists_and_int(a):
    x = 0
    for i in a:
        if isinstance(i, int):
            x += i
        if isinstance(i, list):
            x += summ_of_lists_and_int(i)
    return x


def length_of_words(symbols, repeats):
    result = []
    for i in range(repeats):
        word_index = i % len(symbols)
        result.append(symbols[word_index])
    return result


def generate_password():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''.join(random.choice(alphabet) for _ in range(4))
    return password
