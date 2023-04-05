players = [("Messi",10,1982),("Ronaldo",7,1980),("Lewandowski",9,1985)]
print(players[0])

from collections import namedtuple
football = namedtuple('football','name number age')
dictic = [football("Messi",10,1982),("Ronaldo",7,1980),("Lewandowski",9,1985)]
print(dictic)
print(dictic[0])