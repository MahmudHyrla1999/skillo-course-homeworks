class Student:
    def __init__(self, name, age):
        self.__name = name  # private attribute for name
        self.__age = age  # private attribute for age

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        self.__age = age


# Demonstration of usage
if __name__ == "__main__":
    # Create a Student object
    student1 = Student("Alice", 20)

    # Access and print the attributes using the getter methods
    print("Student name:", student1.get_name())
    print("Student age:", student1.get_age())

    # Update the attributes using the setter methods
    student1.set_name("Bob")
    student1.set_age(22)

    # Access and print the updated attributes
    print("Updated student name:", student1.get_name())
    print("Updated student age:", student1.get_age())
