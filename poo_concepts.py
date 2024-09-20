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

dog = Dog(name='Cat')
cat = Cat(name='Dog')

print('\nExample of Polymorphism:')
animals = [dog, cat]

for animal in animals:
  print(f'The animal {animal.name} speaks {animal.speak()}')

print('\nExample of Encapsulation.')
class BankAccount:
  def __init__(self, balance) -> None:
    self.__balance = balance # private property
  
  def deposit(self, value):
    if value > 0:
      self.__balance += value
  
  def withdraw(self, value):
    if value > 0 and value <= self.__balance:
      self.__balance -= value
    
  def get_balance(self):
    return self.__balance
  
account = BankAccount(1000)
print(f'Balance account: {account.get_balance()}')
account.deposit(500)
print(f'Balance account: {account.get_balance()}')
account.deposit(-500)
print(f'Balance account: {account.get_balance()}')
account.withdraw(200)
print(f'Balance account: {account.get_balance()}')