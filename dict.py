#dictionaries more like Hash

student = {} #empty dictionary
student = {"Alice": 25, "Tom": 23, "Dick": 56}

student["Alice"]  #retrieves the value
student["Alice"] = 26 #assigns a new value

#delete an pair
del student["Tom"]

#extract all the keys
student.keys()

#Convert the above keys to a list to index
list(student.keys())

#extract all the values
student.values()

#Convert the above values to a list to index
list(student.values())
