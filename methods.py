import random

class Cent: #starts with a caps just the same shit again
    def __init__(self, rare=False): #assigns the value to all the objects at the time of instanciation
            if rare:
                self.value = 1.25
            else:
                self.value = 1
            self.color = 'copper'
            self.diameter = 0.75 #inch
            self.thickness = 0.0598 #inch
            self.heads = True

    def __del__(self): #destroys an object when called on
            print("Coin spent!!!")

    def rust(self):
            self.color = "dirty"

    def flip(self):
            coin_head = [True,False]
            choice = random.choice(coin_head) #calls the random lib using the choice method
            self.heads = choice

    def clean(self):
            self.color = 'copper'

p = Cent()
print(p.color)
p.rust()
print(p.color)
p.clean()
print(p.color)
p.flip()
print(p.heads)
#del p
