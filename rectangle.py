class rectangle:
    def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

r1=rectangle(2,4)    

print('Area:',r1.area())
print('perimeter:',r1.perimeter())