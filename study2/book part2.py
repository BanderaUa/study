import math




# class Apple():
#     def __init__(self,w,c,s,t):
#          """вес в граммах"""
#          self.weight = w
#          self.color = c
#          self.shape = s
#          self.taste = t
#          print("Cоздано!")
#
# aplle1 = Apple(100,"Green","Round","Sweat")


class Circle():
     def __init__(self, r):
        self.radius = r
        print("Круг создан c радиусом :" + str(self.radius))

     def ploshad_kruga(self,pls):
          self.ploshad = pls
          self.area = self.ploshad **2 *math.pi
          print(self.area)


ex1 = Circle(5)


