class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
  
  def welcome(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old"

person1 = Person("John", 38)
print("Name: ", person1.name)
print("Age: ", person1.age)
message = person1.welcome()
print(message)

person2 = Person(name="Walter", age=61)
message = person2.welcome()
print(message)