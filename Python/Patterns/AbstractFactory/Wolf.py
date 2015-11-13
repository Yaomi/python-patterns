import Herbivore
import Carnivore

class Wolf(Carnivore.Carnivore):
    
    def Eat(self, herbivore:Herbivore):
        print("{0} eats {1}".format(type(self).__name__, type(herbivore).__name__))


