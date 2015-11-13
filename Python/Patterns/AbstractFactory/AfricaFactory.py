import ContinentFactory
import Wildbeest
import Lion

class AfricaFactory(ContinentFactory.ContinentFactory):
    
    def CreateCarnivore(self):
        return Lion.Lion()

    def CreateHerbivore(self):
        return Wildbeest.Wildbeest()



