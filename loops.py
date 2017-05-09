#while
# while condition:
#     <code here>

number = 1

while number <= 99:
    if (number % 2 == 0):
        print(number)
    number = number + 1
##

name = []
while len(name) < 4:
    j = input("Enter your name: ").strip().capitalize()
    name.append(j)
print("Sorry room is full")
print(name)

#python is a crazy bastard, indenting is important
#to the level of code execution and its meaning
