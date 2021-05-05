from regression_framework.admins.base_admin import Base_admin
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import random

class Logistic_admin(Base_admin):
    def __init__(self,alpha,beta,models):
        super().__init__(alpha,beta,models)
        self.results = {'model': list(), 'fitness' : list()}

    def run_admin(self):
        current_values = None
        regression = 0
        for i in range(9):
            if(i < 5):
                current_values,fitness = self.models[i].run_model(self.beta,current_values)
                self.results['model'].append(i)
                self.results['fitness'].append(fitness)
            else:
                regression = self.execute_regression(i)
                model = regression
                current_values,fitness = self.models[model].run_model(self.beta,current_values)
                self.results['model'].append(model)
                self.results['fitness'].append(fitness)
            print(i)
        print(current_values)
        print('esto es el fitness ',self.models[0].optimization_problem.calcule_fitness(current_values[0]))


    def execute_regression(self,iteration):
        function = 0
        log = LogisticRegression(solver = 'lbfgs')
        try:
            log.fit(self.results['model'],self.results['fitness'])
            function = log.predict(self.results['fitness'])[0]
        except ValueError:
            function = random.randint(0, 2)
        return function
        