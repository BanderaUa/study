players = {
    'Messi' : 10,
    'Suarez' : 9,
    'Ronaldo' : 7,
    'Xavi' : 6,
    'Iniesta' : 8
}

print(players)
# top = players['Messi']
# print('Number on t-shirt is : {top}')
players["Neuer"] = 1
print(players)

for k, v, in players.items():
    print(k,v)