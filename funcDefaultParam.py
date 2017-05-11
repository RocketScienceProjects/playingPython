def about(name, age, likes):
    print("Meet {}, he is {} & likes {}".format(name, age, likes))

about("Ali", 19, "singing")

#assinging default parameter
#note: the parameter with default should be on the right most side!!
def about(name, age, likes="football"):
    print("Meet {}, he is {} & likes {}".format(name, age, likes))

about("Rob", 29)

#all the parameters can have default values if required
def about(name = "Niristotle", age = 29, likes="coding"):
    print("Meet {}, he is {} & likes {}".format(name, age, likes))

about()
