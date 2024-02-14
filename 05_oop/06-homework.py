from abc import ABC, abstractmethod


class Vehicle(ABC):
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine... ")


class Bicycle(Vehicle):
    def start_engine(self):
        print("Pedaling to start bicycle..")


if __name__ == "__main__":
    car = Car()
    bicycle = Bicycle()

    print("Starting the car engine")
    car.start_engine()

    print("Starting Bicycle")
    bicycle.start_engine()
