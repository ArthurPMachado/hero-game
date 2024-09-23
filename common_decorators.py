class MyClass:
  value = 10

  def __init__(self, name) -> None:
    self.name = name
  
  def instance_method(self):
    return f'Instance method call to {self.name}'
  
  @classmethod
  def class_method(cls):
    return f'Class method called to value={cls.value}'
  
  @staticmethod
  def static_method():
    return 'Static method called'


object = MyClass('Class example')
print(object.instance_method())
print(MyClass.value)
# Myclass.instance_method() will throw an Error
print(MyClass.class_method())
print(MyClass.static_method())


class Car:
  def __init__(self, make, model, year) -> None:
    self.make = make
    self.model = model
    self.year = year
  
  @classmethod
  def create_car(cls, configuration):
    # configuration_list = configuration.split(',')
    # make = configuration_list[0]
    # model = configuration_list[1]
    # year = configuration_list[2]
    make, model, year = configuration.split(',')
    return cls(make, model, int(year))

configuration1 = 'Toyota,Corolla,2022'
car1 = Car.create_car(configuration1)

print(f'Make: {car1.make}\nModel: {car1.model}\nYear: {car1.year}')

class Calculator:
  @staticmethod
  def sum(a, b):
    return a + b
  
print(Calculator.sum(5, 9))