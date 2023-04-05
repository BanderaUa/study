palochki = int(10)
"""первый ход"""
player1 = print('Игрок 1: Уберите от 1 до 3 палочек: ')
hod1 =(int(input()))
result1 = print('Осталось палочек : ')
result2 = print(palochki - hod1)
palochki2= palochki - hod1

"""второй ход"""
player2 = print("Игрок 2 : Уберите от 1 до 3 палочек")
hod2 =(int(input()))
result3 = print('Осталось палочек : ')
result4 = print(palochki2 - hod2)
palochki3 = palochki2 - hod2
"""третий ход"""

player1 = print('Игрок 1: Уберите от 1 до 3 палочек: ')
hod3=(int(input()))
result5 = print('Осталось палочек :')
result6 = print(palochki3 - hod3)
palochki4 = palochki3 -hod3
"""четвёртый ход"""
player2 = print("Игрок 2 : Уберите от 1 до 3 палочек")
hod4=(int(input()))
if hod4 >= palochki4:
    print("Игрок 2 : Вы проиграли")
else:
    result7 = print("Осталось палочек :")
result8 = print(palochki4 - hod4)
palochki5 = palochki4 - hod4

"""пятый ход"""
player1 = print("Игрок 1 : Уберите от 1 до 3 палочек")
hod5=(int(input()))
if hod5 >= palochki5:
    print("Игрок 1 : Вы проиграли")
else:
    result9 = print("Осталось палочек :")
result10 = print(palochki5 - hod5)
palochki6 = palochki5 - hod5
"""шестой ход"""
player2 = print("Игрок 2 : Уберите от 1 до 3 палочек")
hod6=(int(input()))
if hod6 >= palochki5:
    print("Игрок 2 : Вы проиграли")
else:
    result11 = print("Осталось палочек :")
result12 = print(palochki6 - hod6)
palochki7 = palochki6 - hod6
"""седьмой ход"""

player1 = print("Игрок 1 : Уберите от 1 до 3 палочек")
hod7=(int(input()))
if hod7 >= palochki7:
    print("Игрок 1 : Вы проиграли")
else:
    result13 = print("Осталось палочек :")
result14 = print(palochki7 - hod7)
palochki8 = palochki7 - hod7

"""восьмой ход"""
player2 = print("Игрок 2 : Уберите от 1 до 3 палочек")
hod8=(int(input()))
if hod8 >= palochki8:
    print("Игрок 2 : Вы проиграли")
else:
    result15 = print("Осталось палочек :")
result16 = print(palochki8 - hod8)
palochki9 = palochki8 - hod8
"""девятый ход"""

player1 = print("Игрок 1 : Уберите от 1 до 3 палочек")
hod9=(int(input()))
if hod9 >= palochki9:
    print("Игрок 2 : Вы проиграли")
else:
    result17 = print("Осталось палочек :")
result18 = print(palochki9 - hod9)
palochki10 = palochki9 - hod9

"""десятый ход"""
player2 = print("Игрок 2 : Уберите от 1 до 3 палочек")
hod10=(int(input()))
if hod10 >= palochki10:
    print("Игрок 2 : Вы проиграли")
else:
    result19 = print("Осталось палочек :")
result20 = print(palochki10 - hod10)
