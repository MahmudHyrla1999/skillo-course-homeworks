class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department


if __name__ == "__main__":
    emp = Employee("Mahmud Hayrula", 6000)

    print("Employee name:", emp.get_name())
    print("Employee Salary", emp.get_salary())
    emp.set_name("Nevrie Hayrula")
    emp.set_salary(60000)

    print("Updated Employee name:", emp.get_name())
    print("Updated Employee Salary:", emp.get_salary())

    manager = Manager("Mahmud", 80000, "Production")

    print("Manager name:", manager.get_name())
    print("Manager salary:", manager.get_salary())
    print("Manager department:", manager.get_department())
    manager.set_department("Desigh")
    print("Updated Manager department:", manager.get_department())
