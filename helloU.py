#ask name
name = input('what the fuck is your name?: ')
#ask age
age = input('what the fuck is your age?: ')

#ask for city
city = input('where the fuck do you live?: ')

#ask what they enjoy
love = input('where the fuck do you enjoy doing?: ')

#create text

string = "Your fucking name is {}, your fucking age is {}, you live in {} and you fucking love {}"
out = string.format(name, age, city, love)

#print out data
print(out)
