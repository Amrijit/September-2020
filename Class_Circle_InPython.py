class cirle:
    
    def __init__(self,r): 
        self.r=r
    def set_radius(self, r):
        self.r=r
    def get_radius(self):
        return self.r
    def getArea(self,r):
        return 3.1416*pow(r,2)
    def getCircumference(self,r):
        return 2*3.1416*r


x=int(input("enter the radius of your circle :"))
c1=cirle(x)
print("The radius of the circle is -> {}".format(c1.get_radius()))
print("The area of the cirle is -> {}".format(c1.getArea(x)))
print("the circumference of the cirle is -> {}".format(c1.getCircumference(x)))

y=int(input("enter anoter radius :"))
c1.set_radius(y)
print("after new asigning, area is {}".format(c1.getArea(y)))
print("after new asigning, circumference is {}".format(c1.getCircumference(y)))
print("after new asigning, radius is {}".format(c1.get_radius()))
