from regression_framework.functions.base_function import Base_function
import numpy as np
import random
from cec2013lsgo.cec2013 import Benchmark


class Shifted_elliptic_function(Base_function):
    def __init__(self,name = 'Shifted_elliptic_function',lower_bound = -100,upper_bound = 100,dimension = 100):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        bench = Benchmark()
        fun_fitness = bench.get_function(1)
        return fun_fitness(x)

    def random_solution(self):
        bench = Benchmark()
        info = bench.get_info(1)
        dim = info['dimension']
        return info['lower']+np.random.rand(dim)*(info['upper']-info['lower'])

    def calcule_fitness(self,value):
        return self.get_fitness(value)