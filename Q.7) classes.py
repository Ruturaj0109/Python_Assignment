class Animal :
    animal_name = ""
    no_of_legs = 0
    color = ""

    def __init__(self, animal_name, no_of_legs, color):
        self.animal_name=animal_name
        self.no_of_legs=no_of_legs
        self.color=color

    def moving():
        print("Animal Moves")

    def eating():
        print("Animal eats")

    def __repr__(self):
        return f"Name: {self.animal_name}, Color: {self.color}"
    
class Human(Animal):
    iq = 0

    def __init__(self, animal_name, no_of_legs, color, iq):
        super().__init__(animal_name, no_of_legs, color)
        self.iq = iq

class Dog(Animal):
    breed = ""

    def __init__(self, animal_name, no_of_legs, color, breed):
        super().__init__(animal_name, no_of_legs, color)
        self.breed = breed

class Cat(Animal):
    breed = ""

    def __init__(self, animal_name, no_of_legs, color, breed):
        super().__init__(animal_name, no_of_legs, color)
        self.breed = breed

class Tiger(Animal):
    subspecies = ""

    def __init__(self, animal_name, no_of_legs, color, subspecies):
        super().__init__(animal_name, no_of_legs, color)
        self.subspecies = subspecies

human = Human(animal_name="Human", no_of_legs=2, color="brown", iq=100)
dog = Dog(animal_name="Dog", no_of_legs=4, color="Black", breed= "Siberian Husky")
cat = Cat(animal_name="Cat", no_of_legs=4, color="White", breed= "Persian")
tiger = Tiger(animal_name="Tiger", no_of_legs=4, color="Yellow-Black", subspecies="Bengal Tiger")

print(human)
print(dog)
print(cat)
print(tiger)