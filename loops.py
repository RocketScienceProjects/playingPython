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

#FOR loops
#range(1,11) doesn't include the 11 here in this range
#difference between py2 abd py3 w.r.t range. In python3, the range is of type 'range' while in py2, the range gives a List

# Python 3.5.2 (default, Nov 17 2016, 17:05:23)
# [GCC 5.4.0 20160609] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> p = range(1,11)
# >>> p
# range(1, 11)
# >>> type(p)
# <class 'range'>
#
# Python 2.7.12 (default, Nov 19 2016, 06:48:10)
# [GCC 5.4.0 20160609] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> p = range(0,10)
# >>> p
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> type(p)
# <type 'list'>

n = range(1,11)
for number in n:
    print(number) 
