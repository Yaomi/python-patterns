import ContinentFactory
import Bison
import Wolf

class AmericaFactory(ContinentFactory.ContinentFactory):
    
    def CreateCarnivore(self):
        return Wolf.Wolf()

    def CreateHerbivore(self):
        return Bison.Bison()

    
