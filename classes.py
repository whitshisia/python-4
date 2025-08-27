# Assignment 1: Inheritance Challenge
# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Inherited class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
    
    def make_call(self, contact):
        print(f"📞 Calling {contact} from {self.device_info()}...")
    
    def charge(self):
        print(f"🔋 Charging {self.device_info()}... Battery now full!")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", "4000mAh")
phone2 = Smartphone("Samsung", "Galaxy S23", "512GB", "4500mAh")

# Using methods
phone1.make_call("Alice")
phone2.charge()


# Assignment 2: Polymorphism Challenge
class Animal:
    def move(self):
        pass  # generic action (to be overridden)

class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("🐦 The bird flies in the sky.")

class Fish(Animal):
    def move(self):
        print("🐟 The fish swims in the water.")

# Create objects
dog = Dog()
bird = Bird()
fish = Fish()

# Polymorphism in action
animals = [dog, bird, fish]
for animal in animals:
    animal.move()

