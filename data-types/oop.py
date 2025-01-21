# object oriented programming
# Defining Classes
class Dog:
    species = "carnivore"#Attribute
    def __init__(self, name, age):# init initialises the functions for us
        self.name = name   #age and name are simply parameters
        self.age = age
dog1 = Dog("Cloppy", 3)#instance of a class variable
dog2 = Dog("Sawyer", 6)

print(Dog.species)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


class Blueprint:
    House = "mansion"
    def __init__(self, material, bedrooms):
        self.material = material
        self.bedrooms = bedrooms
house1 = Blueprint("Brick", 8)
print(Blueprint.House)
print(house1.bedrooms, house1.material)

class Car:
    model ="audi"
    def __init__(self, year, colour, country):
        self.year = year
        self.colour = colour
        self.country = country
car1 =  Car(2014, "red","mateblack")  
print(Car.model) 
print(car1.year,car1.country,car1.colour)   
    


