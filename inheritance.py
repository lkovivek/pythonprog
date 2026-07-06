class Animal:
    # attribute name and method of parent class
    name=""

    def eat(self):
        print("I can eat")
    
# Inherit from Animal
class dog(Animal):
    #new method in subclass
    def display(self):
        print(f'My name is {self.name}')

# create an object of the subclass
labrador=dog()
labrador.name="Bruno"
labrador.display()

# call subclass method
labrador.eat()