#unpack to iterable elements // works in strings as well
nums = [1,2,3,5,6,4]
print(nums)
#gives [1, 2, 3, 5, 6, 4]
print(*nums)
#gives 1 2 3 5 6 4

str = "abcdef"
print(str)
#gives abcdef
print(*str)
#gives a b c d e f
################################
#packing- used in undefined number of parameters
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

#################################
#keyword args (kwargs)

my_dict = {"Name": "Arie", "Age": 1, "Sex": "male"}

def about(Name,Age,Sex):
    return("{} is {} month old and is a {}".format(Name,Age,Sex))

about(**my_dict)  ##note the ** for keyword arguments

##################################

def something(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

something(male = "Ali", female = "Zii")
