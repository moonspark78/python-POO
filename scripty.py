class Dog: 
    def __init__(self, name, breed, owner): 
        self.name = name 
        self.breed = breed
        self.owner = owner
        

    def bark(self): 
        print("Woof!")

class Owner:
    def __init__(self, name, adress, contact_number):
        self.name = name #attribute
        self.adress = adress
        self.contact_number = contact_number

owner1 = Owner("John Doe", "123 Main St", "555-1234")

dog1 = Dog("Buddy", "Golden Retriever", owner1)
#print(dog1.owner.name)

owner2 = Owner("Jane Smith", "456 Elm St", "555-5678")
dog2 = Dog("Max", "Beagle", owner2)
#print(dog2.owner.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30) # Creating an instance of Person class
# person1.greet()

person3 = Person("Bob", 25)
# person3.greet()



""" Different ways to access data and modify it in object """
# Accessing and Modifying Data
# 1. The traditional way: make the data private and use getters ans setters


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip()


user1 = User("theo", " Theo@gmail.com ", "pass123")
user2 = User("anna", " ana@gmail.com. ", "pass456")


# Accessing attributes directly
# print(user1.username)  # Output: theo

#user1.say_hello(user2)  # Output: Sending message to anna : Hi anna, it's theo!

""" print(user1.email)  
user1.email = "new_email@gmail.com"
print(user1.email)   """

""" MAIS ca c'est pas la bbonne facon de faire parce queje peut mettre un no-email adress """

print(user1._email)
print(user1.clean_email())

print(user2._email)
print(user2.clean_email())