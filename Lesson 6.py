# from abc import ABC, abstractmethod
#
# class Country(ABC):
#
#   @abstractmethod
#   def get_name(self):
#     pass
#
#   @abstractmethod
#   def get_capital(self):
#     pass
#
#   @abstractmethod
#   def get_language(self):
#     pass

class Country:
  def __init__(self, name, population, budget):
    self.name = name
    self._population = population
    self.__budget = budget

  def calculate_birth_rate(self):
    pass

  def calculate_death_rate(self):
    pass

  def get_growth_rate(self):
    pass


class Georgia(Country):
  def __init__(self, population, budget):
    super().__init__("Georgia", population, budget)

  def calculate_birth_rate(self):
    print(f"Georgia's birth rate needs to be implemented")

  def calculate_death_rate(self):
    print(f"Georgia's death rate needs to be implemented")

  def get_growth_rate(self):
    print(f"Georgia's growth rate needs to be implemented")


georgia = Georgia(10_000_000, 100_000_000)

georgia.calculate_birth_rate()
georgia.calculate_death_rate()
georgia.get_growth_rate()

print(f"Georgia's name: {georgia.name}")

print(f"Georgia's population: {georgia._population}")
# print(f"Georgia's budget: {georgia.__budget}")