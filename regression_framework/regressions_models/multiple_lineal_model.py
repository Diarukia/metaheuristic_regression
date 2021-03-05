from regression_framework.metaheuristics.sho import Sho
import numpy as np
import random

class Multiple_lineal_model:
    def __init__(self):
        self.metaheuristic_target = None
        self.infactsol = 0
        self.factsol = 0
        self.imprperc = 0
        self.parameter_model = {'PercFactSol': None, 'PercInfactSol' : None, 'ImprPerc' : None}
        self.roulette = [0.2,0.2,0.2,0.2,0.2]

    def run_model(self):
        pass

    def aceptation_criteria(self, value_1, value_2):
        if self.opt(value_1)<self.opt(value_2):
            self.factsol += 1
        else:
            self.infactsol += 1
            return False
        return True

    def roulette_function(self,poblation_number,poblation_values,current_iterations,random_solution):
        if(current_iterations % 10 == 0):
            n = random.random()
            amount = 0
            for i in range(5):
                n = n-self.roulette[i]
                amount = amount + 20
                if n <= 0:
                    break
            poblation_number = amount
            poblation_values = modify_poblation(poblation_number,poblation_values,random_solution)

        return poblation_number,poblation_values

    def modify_poblation(self,poblation_number,poblation_values):
        while(poblation_number < len(poblation_values)):
            poblation_values.pop()
        while(newPoblation > len(poblation_values)):
            poblation_values.append(random_solution())
        return poblation_values
