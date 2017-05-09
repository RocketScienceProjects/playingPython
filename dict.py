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
#######################
#list with dictionary#
employees = {
    "Alice": [100, 25, "HR" ],
    "Tom": [200, 23, "DEV"],
    "Dick": [300, 56, "SALES"]
    }
print(employees["Alice"][0])
print(employees["Tom"][2])

#dictionary inside dictionary
employees = {
    "Alice": {"EID": 100, "Age": 25, "Dept": "HR"},
    "Tom": {"EID": 200, "Age": 23, "Dept": "DEV"},
    "Dick": {"EID": 300, "Age": 56, "Dept": "SALES"}
    }
print(employees["Alice"]["EID"])
print(employees["Tom"]["Age"])
