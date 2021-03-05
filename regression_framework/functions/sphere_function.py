from regression_framework.functions.base_function import Base_function
import numpy as np
import random

class Sphere_function(Base_function):
    def __init__(self,name = 'Sphere_function',lower_bound = -100,upper_bound = 100,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        return sum(x**2)

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution

