# NameError: name 'Pet' is not defined. Did you mean: 'set'?
# import pet_class
class Pet:
    energy = 100
    health = 100
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
    def sleep(self):
        self.energy += 25
        print(f"Energy: {self.energy}")
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Energy: {self.energy} Health: {self.health}")
    def play(self):
        self.health  = self.health + 5
        print(f"Health: {self.health}")
        return self
    def noise(self):
        # print(self.type)
        if (self.type == 'Dog'):
            print('woof')
        elif (self.type == 'Cat'):
            print('meow')
        elif (self.type == 'Dragon'):
            print('grumble')
        elif (self.type == 'Phoenix'):
            print('inaudible')
        return self
    def display_self(self):
        print(f"Name: {self.name} Type: {self.type} Tricks: {self.tricks} Energy: {self.energy} Health: {self.health}")
Odin = Pet('Odin', 'Dog', 'Shake')
# print(Odin.type)
# Odin.sleep()
# Odin.eat()
# Odin.play()
# Odin.noise()

# class Cat(Pet):
#     energy = 50
#     health = 900
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)
#         type = 'Cat'
# Floofy = Cat('Floofy', 'Cat', 'Ignore')
# print(Floofy.type)
# Floofy.sleep()
# Floofy.eat()
# Floofy.play()
# Floofy.noise()

# class Dragon(Pet):
#     energy = 500
#     health = 120000
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)
#         type = 'Dragon'
# Smaug = Dragon('Smaug', 'Dragon', 'Ignore')
# print(Smaug.type)
# Smaug.sleep()
# Smaug.eat()
# Smaug.play()
# Smaug.noise()

# class Phoenix(Pet):
#     energy = 5
#     health = 120000
#     def __init__(self, name, type, tricks):
#         super().__init__(name, type, tricks)
#         type = 'Phoenix'
# Fawkes = Phoenix('Fawkes', 'Phoenix', 'Rebirth')
# print(Fawkes.type)
# Fawkes.sleep()
# Fawkes.eat()
# Fawkes.play()
# Fawkes.noise()

class Ninja(Pet):
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.type = Odin.type
    def walk(self):
    # invoke pet play method here
        super().play()
    def feed(self):
    # invoke pet eat method here
        super().eat()
    def bathe(self):
    # invoke pet noise method here
        super().noise()
# to use an instance the instance must be referenced in the same file?
Jake = Ninja('Bob', 'Crombobolis', Odin, 'peanut_butter', 'Purina')
print(Jake.first_name, Jake.last_name, Jake.pet, Jake.treats, Jake.pet_food)
Jake.walk()
Jake.eat()
Jake.bathe()
# below won't work because bathe is a method from ninja not pet
# Odin.bathe()