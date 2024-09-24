# Character: parent class
# Hero: controlled by player
# Enemy

class Character:
  def __init__(self, name, health, level) -> None:
    self.__name = name
    self.__health = health
    self.__level = level
  
  def get_name(self):
    return self.__name
  
  def get_health(self):
    return self.__health
  
  def get_level(self):
    return self.__level

  def show_details(self):
    return f'Name: {self.get_name()}\nLife: {self.get_health()}\nLevel: {self.get_level()}'

class Hero(Character):
  def __init__(self, name, health, level, special) -> None:
    super().__init__(name, health, level)
    self.__special = special
  
  def get_special(self):
    return self.__special

  def show_details(self):
    return f'{super().show_details()}\nSpecial: {self.get_special()}\n'

class Enemy(Character):
  def __init__(self, name, health, level, type) -> None:
    super().__init__(name, health, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f'{super().show_details()}\nType: {self.get_type()}\n'

hero = Hero('Hero', 100, 5, 'Flash Strike')
print(hero.show_details())

enemy = Enemy('Bat', 50, 3, 'flyer')
print(enemy.show_details())