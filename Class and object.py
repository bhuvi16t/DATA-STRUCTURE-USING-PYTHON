# DSA ASSESMENT -2 

# 1. Define a python class Person with instance object variables name and age. Set
# Instance object variables in _init_() method. Also define show() method to display
# name and age of a person.

class Person :

    def __init__(self,name, age) :
        self.name = name 
        self.age = age
    
    def show(self):
        print(f'The Person Name is : {self.name} and age is :{self.age}')
    
    def setName(self,name):
        self.name = name
       
    def setAge(self,age):
        self.age = age

    def getName(self):
        print(self.name)  

    def getAge(self):
        print(self.age)   

per1=Person('Bhoopendra',18)
per2=Person('rahul',18)
per3=Person('yogesh',18)
per1.setAge(21)
per1.show()
per2.getName()

# 2. Define a class Circle with instance object variable radius. Provide setter and getter for radius. 
# also define getArea() and getCircumference() methods.

class Circle :

    def __init__(self,radius):
        self.radius = radius

    def setRadius(self,radius):
        self.radius= radius

    def getRadius(self):
        print('Radius is :', self.radius)

    def getArea(self):
        print( f'The Area of Circle is :{ 3.14 * self.radius**2 } ')

    def getCircumference(self):

        print( f'The cercumference of the circle is : {2 *  3.14 * self.radius}')

c1=Circle(6.5)
c1.getArea()
c1.getCircumference()

# 3. Define a class Rectangle with length and breadth as instance object variables. 
# Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle :

    def __init__(self, lenghth,bridth):

        self.lenghth= lenghth
        self.bridth= bridth
    
    def setDimensions(self,lenghth,bridth):
        self.lenghth= lenghth
        self.bridth= bridth

    def showDimensions(self):
        print(f' The lenght is : {self.lenghth} and bridth is  {self. bridth}')

    def showArea(self) :
        print(f'The Area is : {self.lenghth * self.bridth }')  


rect1=Rectangle(6,5)
rect1.setDimensions(4,2)
rect1.showDimensions()
rect1.showArea()