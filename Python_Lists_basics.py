known_users=["Alice","Bob","Claire","Dan", "Emma", "Fred", "Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi!")
    name = input("What is your name?").strip().capitalize()

    if name in known_users: 
        print("Hello {}!".format(name))
        answer = input("Would you like to be removed from the list?").strip().lower()
        if answer == "yes":
            known_users.remove(name)
    

    else:
        print("name not recognised")
        answer = input("Would you like to be added to the list?").strip().lower()
        if answer == "yes":
            known_users.append(name)

    print(known_users)
