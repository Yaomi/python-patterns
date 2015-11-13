import Herbivore
import Carnivore
import ContinentFactory

class AnimalWorld(object):
    def __init__(self, continentFactory:ContinentFactory):
        self.herbivore = continentFactory.CreateHerbivore()
        self.carnivore = continentFactory.CreateCarnivore()

    def RunFoodChain(self):
        self.carnivore.Eat(self.herbivore)

