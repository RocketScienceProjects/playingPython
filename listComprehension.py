#List comprehension is an elegant way to define and create list in Python.
#These lists have often the qualities of sets, but are not in all cases sets.


even_number = [x for x in range(1,14,3) if x%2 == 0]  #range(start, end, step)
print(even_number)
