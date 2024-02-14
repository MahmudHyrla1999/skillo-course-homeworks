class Animal:
    def __init__(self,species):
        self.species = species

class Dog(Animal):
    def __str__(self):
        return f"I'm a Dog member of the {self.species} species."


class Cat(Animal):
    def __str__ (self):
        return f" I'm a Cat member of the {self.species} species."

if __name__ == "__main__":
    dog = Dog("Canis lupus caniliaris")
    cat = Cat("Felis Catus")

    print(dog)
    print(cat)
