from datetime import datetime

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
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email




#user1 = User("theo", "theo@gmail.com", "pass123")
#print(user1.get_email())  # Accessing email using getter method

#user1.set_email("eline17@2679")  # Modifying email using setter method
#print(user1.get_email())  # Accessing updated email using getter method




# .2 Properties

class Car:
    def __init__(self, brand, model, year, email):
        self.brand = brand
        self.model = model
        self.year = year
        self._email = email
        
    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
my_car = Car("Tesla", "Model 3", 2024, "tesla@gmail.com")
my_car.email = "this is not a year"
# print(my_car.email)
        




"""  ------------- Static. Attributes ------------- """
# A static attiribute ( sometimes called a class attribute) is an attribute that belongs to the class itself, not to any specific instance of the class.

class User:
    user_count = 0  # Static attribute to keep track of the number of users

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1  # Increment user count when a new user is created

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")
        
# Creating instances of User class
user1 = User("alice", "alice@gmail.com")
user2 = User("bob", "bobo@gmail.com")

# print(f"Total users: {User.user_count}")  # Accessing static attribute via class name
# print(f"Total users: {user1.user_count}")  # Accessing static attribute via instance (not recommended)
# print(f"Total users: {user2.user_count}")  # Accessing static attribute via instance (not recommended)


"""  ------------- Static. Methods ------------- """
# A static method is a method that belongs to the class rather than any specific instance of the class. It does not have access to instance-specific data (i.e., it cannot access self).

class BankAccount:
    MIN_BALANCE = 100  # Static attribute
    
    def __init__(self, onwer, balance=0):
        self.owner = onwer
        self._balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction("deposit", amount)
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")
            
    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balence: $ {self._balance}")
    
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5  # Valid interest rate is between 0 and 5 (inclusive)
    
# account = BankAccount("Charlie", 500)
# account.deposit(200)

#account.__log_transaction("withdraw", 300)  # This will raise an AttributeError

# print(BankAccount.is_valid_interest_rate(3))  # True
# print(BankAccount.is_valid_interest_rate(7))  # False
# print(account.is_valid_interest_rate(4))  # True (can also be called on an instance, but not recommended)




""" ------------- Encapsulation ------------- """

""" 
Encapsulation provides several benefits:

        Data Protection: Prevents accidental modification of data
        Validation: You can validate data before setting it
        Flexibility: Internal implementation can change without affecting external code
        Control: You have full control over how data is accessed and modified
"""

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance
        

#account = BadBankAccount(0.0)
#account.balance = -1
#print(f"BadBankAccount balance: {account.balance}")  # Output: -1 (invalid state)

class GoodBankAccount:
    def __init__(self):
        self._balance = 0.0  # Private attribute
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount.")
            

test_account = GoodBankAccount()
#print(test_account.balance)  
test_account.deposit(1.99)
#print(test_account.balance) 
test_account.withdraw(1)
#print(test_account.balance)



""" ------------- Absraction ------------- """
class EmailService:
    
    def connect(self):
        print("Connecting to email server...")
    
    def authenticate(self):
        print("Authenticating...")
        
    def send_email(self):
        self.connect()
        self.authenticate()
        print("Sending email...")
        self.disconnect()
        
    def disconnect(self):
        print("Disconnecting from email server...")

#email = EmailService()
#email.connect()
#email.authenticate()
#email.send_email()
#email.disconnect()


""" ------------- Inheritance ------------- """
""" Inheritance allows a class (called a subclass or derived class) to inherit
    attributes and methods from another class (called a superclass or base class).
    This promotes code reusability and establishes a hierarchical relationship between classes. """
    
    
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year