#Global & local - just the same shit
a = 100

def f1():
    print(a)

def f2():
    print(a)

####
a = 100

def f1():
    a = 45 #local
    print(a)

def f2():
    a = 33 #local
    print(a)

######overriding a global var #########
a = 100

def f1():
    global a #declaring a global variable # global a = 45 , syntax will not work
    a = 45 #setting the value to the new global variable
    print(a)

def f2():
    a = 33 #local
    print(a)

#call the functions
f1()
f2()
print(a)

########################

a = [1,2,3]
#in the case of List and Dict, no need for the global keyword declaration
def f1():
    a[0] = 8 #setting the value to the new global variable
    print(a)

def f2():
    a = 33 #local
    print(a)

#call the functions
f1()
f2()
print(a)
