contacts = {}


contacts["Alice"] = "alice@example.com"
contacts["Bob"] = "bob@example.com"
contacts["Charlie"] = "charlie@example.com"


print("Email for Alice:", contacts["Alice"])
print("Email for Bob:", contacts["Bob"])


contacts["Bob"] = "new_bob@example.com"

del contacts["Charlie"]
print("\nContact List:")
for name, email in contacts.items():
    print(f"{name}: {email}")