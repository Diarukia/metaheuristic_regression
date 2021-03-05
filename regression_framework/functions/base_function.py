from abc import ABC, abstractmethod
import random

class Base_function(ABC):
    def __init__(self,name,lower_bound,upper_bound,dimension):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimension = dimension

    @abstractmethod
    def get_fitness(self,value):
        pass

    @abstractmethod
    def random_solution(self):
        pass

    def calcule_fitness(self,value): # esto es lo unico que la metaheuristica vera
        return self.get_fitness([value for x in range(self.dimension)])

