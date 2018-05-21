from math import pi

class circle:
  def __init__(self,r):
     self.r=r

  def area(self):
      return pi*(self.r**2)

  def perimeter(self):
      return 2*pi*self.r    

c1=circle(4)
print('Area of circle:',c1.area())
print('Perimeter of circle:',c1.perimeter())