from datetime import datetime


class Employee:

    def __init__(self, name, start_date, PIN, phone, address, manager_name, department):
        self._name = name
        self._start_date = start_date
        self._PIN = PIN
        self._phone = phone
        self._address = address
        self._manager_name = manager_name
        self._department = department

    def calculate_tenure(self, tenure=None):
        """Calculate the tenure of the employee in years."""
        start_datetime = datetime.strptime(self._start_date, "%Y-%m-%d")
        current_datetime = datetime.now()
        tart_datetime = datetime.strptime(self._start_date, "%Y-%m-%d")
        current_datetime = datetime.now()

        if current_datetime.month < start_datetime.month or \
                (current_datetime.month == start_datetime.month and current_datetime.day < start_datetime.day):
               tenure -= 1
        return tenure

    def business_card_info_(self):
        """Return a string representation of the employee's business card information."""
        return f"Name: {self._name}\n" \
               f"Start Date: {self._start_date}\n" \
               f"Phone: {self._phone}\n" \
               f"Address: {self._address}\n" \
               f"Manager: {self._manager_name}\n" \
               f"Department: {self._department}"

    def business_card_info(self):
        pass


if __name__ == "__main__":
    emp = Employee("John Doe", "2020-01-01", "123456", "555-1234", "123 Main St", "Jane Smith", "HR")

    print("Employee Tenure:", emp.calculate_tenure(), "years")
    print("Business Card Information:")
    print(emp.business_card_info())