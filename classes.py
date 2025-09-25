class Dog():
    """Class to represent a dog"""
    def __init__(self, name):
        """"Initalizing the object"""
        self.name = name 
    
    def sit (self):
        """Simulating setting"""
        print (self.name + " Is setting")
    
my_dog = Dog ('Pita')
print (my_dog.name + " Is a great dog ")
my_dog.sit()


########################### Inheristance : 

class SearchingDog(Dog):
    """Represnet a search dog"""
    def __init__(self , name):
        """"Initalizing the object"""
        super().__init__(name)
    def searching(self):
        """Simulating searching"""
        print (self.name + " is searchning.")
        
my_dog = SearchingDog ('Wiliam')
print (my_dog.name + " is sreaching")
my_dog.sit()
my_dog.searching()