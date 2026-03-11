import matplotlib.pyplot as plt


class circle(object):
    def __init__ (self,radius=1,color="black"):
        self.radius=radius
        self.color=color
        
    def add(self,r):
        self.radius = self.radius+r
        
    def drawCircle(self):
        circle = plt.Circle((0,0), self.radius, color=self.color)#Circle a shape object takes parameter center,r,color
        plt.gca().add_patch(circle)#gca get current axis and add patch add the circle
        plt.axis('equal')# make sure both axis is same scale
        plt.xlim(-self.radius-1, self.radius+1) #kotodhur dekhabo
        plt.ylim(-self.radius-1, self.radius+1)
        plt.show()

        
circle1=circle(5,"red")
circle2=circle(5,"green")

print(circle1.color)
print(circle2.color)

circle1.radius=6
print(circle1.radius)

circle1.add(10)
print(circle1.radius)

print(dir(circle1))
circle3=circle()
print(circle3.radius)

circle1.drawCircle()
circle2.drawCircle()

class rectangle(object):
    def __init__(self, width=2, height=3, color="red"):
        self.width=width
        self.height=height
        self.color=color
        
    def drawrec(self):
        rec= plt.Rectangle((0,0),self.width,self.height,color=self.color)
        plt.gca().add_patch(rec)
        plt.axis("scaled")
        plt.show()
        
rectangle1=rectangle(2,3,"blue")
rectangle1.drawrec()

