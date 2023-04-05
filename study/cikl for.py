numbers = [1,2,3,4,5]
# print(numbers)

for x in numbers:
    print(x*x)

for i in range(1,6):
   if i % 2== 0:
        print(str(i) + "chetnoe")
   else:
        print(str(i) +"nechetnoe")

numbers2= [1,3,5,7,9]
for i,items in enumerate(numbers2):
    numbers2[i] *= 2
print(numbers2)
