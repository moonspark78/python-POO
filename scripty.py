class Dog: 
    def __init__(self, name, breed, owner): 
        self.name = name 
        self.breed = breed
        self.owner = owner
        

    def bark(self): 
        print("Woof!")

class Owner:
    def __init__(self, name, adress, contact_number):
        self.name = name
        self.adress = adress
        self.contact_number = contact_number

owner1 = Owner("John Doe", "123 Main St", "555-1234")

dog1 = Dog("Buddy", "Golden Retriever", owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)

owner2 = Owner("Jane Smith", "456 Elm St", "555-5678")
dog2 = Dog("Max", "Beagle", owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)