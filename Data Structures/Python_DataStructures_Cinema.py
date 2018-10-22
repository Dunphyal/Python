films = {
    "Finding Dory" : [3,5],
    "Bourne" : [18,5],
    "Tarzan" :[15,5],
    "Ghost Busters" :[12,5]
    }

while True:
    choice = input("Which film would you like to watch?").strip().title()
    if choice in films:
        age=int(input("How old are you?").strip())

        if age >= films[choice][0] and films[choice][1] > 0:
            films[choice][1] = films[choice][1] - 1
            print("Enjoy the film")
        else:
            print("Sorry this cannot be completed")
    else:
        print("Sorry we don't have that film")
