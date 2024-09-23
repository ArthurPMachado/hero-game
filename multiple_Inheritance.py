class Animal:
  def __init__(self, name) -> None:
    self.name = name
  
  def speak(self):
    pass

class Mammal(Animal):
  def breastfeed(self):
    return f'{self.name} is breastfeeding.'

class Bird(Animal):
  def fly(self):
    return f'{self.name} is flying.'

class Bat(Mammal, Bird):
  def speak(self):
    return "Bats emit ultrasonic sounds."

bat = Bat("Bat")

print('Bats name: ', bat.name)
print('Bats sound: ', bat.speak())
print('Bat breastfeeding: ', bat.breastfeed())
print('Bat flying: ', bat.fly())