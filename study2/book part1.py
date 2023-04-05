




# #pervoe zadanie iz knigi
# def square(x):
#     x = int(input("Vvedite chislo:"))
#     return x**2
# a = square(6)
# print(a)


# def stroka(x):
#     x = 'stroka'
#     return x

# def zadanie3(x,y,z,a=1,b=3):
#     result = x+y+z-a-b
#     print(result)
#
#
# zadanie3(2,6,4)

# def pervaya_funkciya(x):
#     result = x / 2
#     print(result)
#
# def vtoraya_funkciya(x):
#     result = x * 4
#     print(result)
# pervaya_funkciya(66)
# resultat = 33
# vtoraya_funkciya(resultat)






# lists = []
# rap= [ '2pac','icecube','eazy-e','notorious big','nwa']
# rock = ['korol i shut','mettalica','linkin park']
# djs = ['paul','tiesto']
#
# lists.append(rap)
# lists.append(rock)
# lists.append(djs)
# print(lists)
#
# rap = lists[0]
# print(rap)
#
# rap.append('lil pump')
# print(rap)
# print(lists)




# my_music = ['ski mask','lil skies','playboy','kendrick']
#
# coordinates = [('36°54′29″ с.ш.' , '30°41′44″ в.д.') , ('50°27′16″ с.ш.' , '30°31′25″ в.д.')]
#
# me_facts = { 'height': '178' , 'fav_colour' : 'black' , 'fav_actor' : 'robert downie jr.' , 'y_o' : '19'}
#
# print('''Если хотите узнать рост введите: 'height'
# Если хотите узнать любимый цвет введите: 'fav_colour'
# Если хотите узнать любимого актера введите: 'fav_actor'
# Если хотите узнать возраст введите: 'y_o' ''')
#
# x = input()
#
# print(me_facts)


# a = 'Felix {}'
# b = str(input())
# c = a.format(b)
# print(c)


# c = "Я сегодня был дома. Потом пошел на тренировку"
# b = c.split('.')
# print(b)


# first_three = 'abc'
# result = '-'.join(first_three)
# print(result)


# a = "Чехов"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# a = "Вчера я написал {}"
# b = "Вчера я ходил {}"
#
# perviy_otvet = str(input("Введите первое предложение : "))
# vtoroy_otvet = str(input("Введите второе предложение : "))
#
# otvet1 = a.format(perviy_otvet)
# otvet2 = b.format(vtoroy_otvet)
#
# print(otvet1)
# print(otvet2)

# 35 34 33
# a = "олдос Хаксли родился в 1894 году"
# b = a.capitalize()
# print(b)

# a = "Где это? Кто это? Когда это?"
# b = [a]
# print(b)

# a = ['lisa', 'prignula' , 'cherez' , 'nizkiy' , 'zabor', '.']
# b = a.pop()
# c = a.pop()
# d = c+b
# e = ' '.join(a)
# f = e + ' ' + d
# print(f)


# a = "Ребенок -  зеркало поступков родителей"
# b = a.replace("о","0")
# print(b)


# tv = ['Breaking bad','big bang theory','Fargo']
# i = 0
# for x in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#     i+=1
#
# print(tv)

# for i in range(0,9999999):
#     print(i)


# x = 10
# while x > 0:
#     print(x)
#     x-=1
# print("C NOVIM GODOM!")


# a = [ 'The Sopranos','Walking dead','Breaking Bad']
# i = 0
# for x in a:
#     i += 1
#
# print(a)

# for i in range(25 ,51):
#     print(i)


# list1 = [8,19,148,4]
# list2= [9,1,33,83]
# list3 = []
# for i in list1:
#     for j in list2:
#         list3.append(i*j)
#
# print(list3)



# import random
# x = random.randint(0,101)
# y = random.randint(0,101)
# z = 11
#
#
# print("Здравствуйте,вы хотите сгенерировать число?")
# chislo = input()
#
# if chislo == "Да":
#     print(x)
# else:
#     print("Неизвестная команда")
#
# print("вы хотите сгенерировать еще одно число?")
# chislo2 = input()
# if chislo2 == "Да":
#     print(y)
# else:
#     print("Неизвестная команда")
#
# print("вы хотите сгенерировать еще одно число?")
# chislo3 = input()
# if chislo3 == "Да":
#     print(z)
# else:
#     print("Неизвестная команда")

# import os
# os.path.join('Users' , 'GameOn Dp','Desktop','bob','pycharm88')

# st = open('pycharm88.txt','w')
# st.write("Privet ot python!")
# st.close()

# with open("pycharm88","w") as f:
#     f.write("Privet ot python!")



# with open("pycharm88","r") as f:
#     print(f.read())


# my_list = list()
# with open("pycharm88","r") as f:
#     my_list.append(f.read())
# print(my_list)


# f = 16
# print(f > 10 or f < 10)


# a = ord('a')
# print(a)

# b = 1
# a = 3
# b += 1
# c = 0

# while a <10:
#     c = c+1
#     print(c)


# age = int(input('Enter your age: '))
# name = input('Enter your name: ')
#
# if age < 18 or name == 'Alice':
#     print('not allowed to drink')
# elif age <= 21 and name == 'Bob':
#     print('not allowed to drink (USA citizen)')
# else:
#     print('allowed to drink')
