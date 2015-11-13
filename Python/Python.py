import sys 
import Singleton
import Director, ConcreteBuilder
import Document, Resume, Report
import ContinentFactory, AnimalWorld, AfricaFactory, AmericaFactory
import IBM, Investor

def main():
    #Creational Patterns
    #singleton()
    #builder()
    #factoryMethod()
    #abstractFactory()
    #Structural Patterns
    #Behavioral Patterns
    observer();
    input("Press Enter to continue...")

def observer():
    print("Observer pattern.")
    ibm = IBM.IBM("IBM", 120.0)
    ibm.Attach(Investor.Investor("Sorros"))
    ibm.Attach(Investor.Investor("Berkshire"))
    ibm.Price = 120.0
    ibm.Price = 121.0
    ibm.Price = 120.5
    ibm.Price = 120.75

def abstractFactory():
    print("Abstract factory pattern.")
    africa = AfricaFactory.AfricaFactory()
    world = AnimalWorld.AnimalWorld(africa)
    world.RunFoodChain()

    america = AmericaFactory.AmericaFactory()
    world = AnimalWorld.AnimalWorld(america)
    world.RunFoodChain()

def factoryMethod():
    print("Factory method pattern.")
    documents = []
    documents.append(Resume.Resume())
    documents.append(Report.Report())

    for doc in documents:
        print("-----{0}-----".format(type(doc).__name__))
        for page in doc.Pages():
            print(page.GetName())

def builder():
    print("Builder pattern.")
    director = Director.Director()
    concreteBuilder = ConcreteBuilder.ConcreteBuilder()
    
    director.Construct(concreteBuilder)
    product = concreteBuilder.GetResult()
    product.Show()

def singleton():
    print("Singleton pattern.")
    singleton1 = Singleton.Singleton()
    singleton2 = Singleton.Singleton()
    if(id(singleton1) == id(singleton2)):
        print("Object are equal.")
    else:
        print("Object are not equal.")

if __name__ == "__main__":
    sys.exit(int(main() or 0))
    