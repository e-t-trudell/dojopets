# import pet_class
class Pet:
    energy = 100
    health = 100
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        type = 'Dog'
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
        print(self.type)
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
class Phoenix(Pet):
    energy = 5
    health = 120000
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        type = 'Phoenix'
Fawkes = Phoenix('Fawkes', 'Phoenix', 'Rebirth')
print(Fawkes.type)
Fawkes.sleep()
Fawkes.eat()
Fawkes.play()
Fawkes.noise()