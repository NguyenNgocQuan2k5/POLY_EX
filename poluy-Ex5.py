class Animal:
    def __init__(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def make_sound(self):
        return "Animal sound"
    
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender}."

class Dog(Animal):
    def make_sound(self):
        return "Bark"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."

class Cat(Animal):
    def make_sound(self):
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."
    
class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."
    
class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "HISS"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}."
