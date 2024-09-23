from typing import Any


def my_decorator(func):
  def wrapper():
    print('Before the function call')
    func()
    print('After the function call')
  
  return wrapper

@my_decorator
def my_function():
  print('My function was called')

my_function()

class MyClassDecorator:
  def __init__(self, func) -> None:
    self.func = func
  
  def __call__(self) -> Any:
    print('Before the function call inside MyClassDecorator')
    self.func()
    print('After the function call inside MyClassDecorator')

@MyClassDecorator
def second_function():
  print('Second function was called')

second_function()