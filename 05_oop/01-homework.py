# Create a class "Person" with a special method "__str__" to provide a string representation.
class Person:

    def __init__(self, name, age, town, weight, height, nationality):
        self.name = name
        self.age = age
        self.town = town
        self.weight = weight
        self.height = height
        self.nationality = nationality

    # Instantiate an object of the Person class
    def __str__(self):
        return f' Name: {self.name}, Age: {self.age}, Town: {self.town}, Weight: {self.weight}, Height: {self.height},Nationality: {self.nationality}'


person1 = Person('Mahmud', 33, 'Plovdiv', 83, 174, 'Bulgarian')

# Print the object
print(person1)
