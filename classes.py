# classes.py
############### Fruit classes ###############
import random

class Fruit():
    def __init__(self):
        self.flavour, self.colour = random.choice(self.varieties)

    def __repr__(self):
        return f"<{self.flavour}, {self.colour} {self.__class__.__name__}>"
    
class Apple(Fruit):
    varieties = [("sour", "green"), ("sweet", "red")]

class Pear(Fruit):
    varieties = [("mellow", "yellow"), ("sharp", "green")]


############## Tree classes #################

class Tree():
    def __init__(self):
        self.fruits = []

    def __repr__(self):
        return f"{self.fruit_type.__name__} tree"

    def blossom(self):
        for i in range(self.fecundity):
            self.fruits.append(self.fruit_type())

    def harvest(self):
        crop = self.fruits
        self.fruits = []
        return crop

class AppleTree(Tree):
    fecundity = 8
    fruit_type = Apple

class PearTree(Tree):
    fecundity = 5
    fruit_type = Pear

############## Cider Class #################

class Cider():
    def __init__(self, fruitlist):
        self.flavour = {
            "sweet": 0,
            "sour": 0,
            "mellow": 0,
            "sharp": 0
        }
        for fruit in fruitlist:
            self.flavour[fruit.flavour] += 1
    
    def __repr__(self):
        return f"a barrel of {max(self.flavour, key=lambda key: self.flavour[key])} cider"

############## Farm Class #################

class Farm():
    def __init__(self) -> None:
        print("Welcome to our farm!\n")
        print("What type of tree do you want to plant?")
        print("1 - Apple    2 - Pear")
        print("Please select 1 or 2: ")
        num_trees = int(input())