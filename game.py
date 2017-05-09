import random

health = 50
difficulty = 1
ph = int(random.randint(25, 50) / difficulty) #type casting to intfrom float
health = health + ph
print(health)
