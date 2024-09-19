# Inheritance
print('\nExample of Inheritance:')
class Animal:
  def __init__(self, name) -> None:
    self.name = name
  
  def walk(self):
    print(f'The animal {self.name} walked')
    return

  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return 'Woof'

class Cat(Animal):
  def speak(self):
    return 'Miau'