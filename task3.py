def register_students(*students):
    print("Registered_Students:")
    for student in students:
        print(student)
    print("Total:", len(students))
register_students("Ali", "Leyla", "Kamran")
