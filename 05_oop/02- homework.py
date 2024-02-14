class Email:
    def __init__(self, address):
        self.address = address

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.address == other.address
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


# Testing the class Email
if __name__ == "__main__":
    # Create email instances
    email1 = Email("example1@example.com")
    email2 = Email("example2@example.com")
    email3 = Email("example1@example.com")

    # Test equality and inequality
    print("Email 1 == Email 2:", email1 == email2)  # False
    print("Email 1 != Email 2:", email1 != email2)  # True
    print("Email 1 == Email 3:", email1 == email3)  # True
    print("Email 1 != Email 3:", email1 != email3)  # False

