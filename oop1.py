class Dollar: #starts with a caps just the same shit again
    value = 1
    color = 'green'
    breadth = 2.61
    length = 6.14

#instancing a class in python
j = Dollar()
k = Dollar()
#check the data type for the objects
print(type(j))
print(type(k))
#accessing the values from the class
print(j.value)
print(k.length)
#override a value in an object
k.length = 7.12
print(k.length)
