k_users = ["Alice", "Tom", "Jack", "Harry", "Salt"]

print(len(k_users))

while True:
    print("Hi, my name is Travis?")
    name = input("whats your name?: ").strip().capitalize()

    if name in k_users:
        print("authorized name")
        print("hello {}.... Good day!!!".format(name))
        rem = input("Do you want to be removed from the system? Enter y/n....").strip().lower()
        if rem == 'y':
            k_users.remove(name)  #remove() and del()
            print("{} removed from the system".format(name))
        elif rem == 'n':
            print("Good .... hang in there!!!")


    else:
        que = input("unauthorized name...Would you like to signed up?... (y/n):" ).strip().lower()
        if que == 'y':
            k_users.append(name)
            print(k_users)
        elif que == 'n':
            print("See you around, good man!")
