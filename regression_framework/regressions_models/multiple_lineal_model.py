from regression_framework.metaheuristics.sho import Sho
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import random
import time
import warnings

class Multiple_lineal_model:
    def __init__(self,optimization_problem):
        self.optimization_problem = optimization_problem
        self.metaheuristic_target = Sho(self.optimization_problem.calcule_fitness,self.aceptation_criteria,0.1514,25,self.optimization_problem.random_solution,self.roulette_function)
        self.infactsol = 0
        self.factsol = 0
        self.imprperc = 0
        self.parameter_model = {'PercFactSol': list(), 'PercInfactSol' : list(), 'ImprPerc' : list()}
        self.roulette = [0.2,0.2,0.2,0.2,0.2]
        self.total_iteration = 100

    def run_model(self,beta):
        current_values = None
        start_time = time.time()
        while(self.total_iteration > 0): #fixme : cuando termina de iterar necesita un reset de los atributos
            if(self.total_iteration/ beta >= 1 ):
                current_values = self.metaheuristic_target.run_metaheuristic(self.metaheuristic_target.poblation_number,self.metaheuristic_target.poblation_values)
                self.total_iteration -= beta
                print()
                print(current_values)
                print()
            else:
                current_values = self.metaheuristic_target.run_metaheuristic(self.metaheuristic_target.poblation_number,self.metaheuristic_target.poblation_values,self.total_iteration)
                self.total_iteration -= self.total_iteration
            self.regression_model()
        return current_values

    def termination_criterion(self):
        self.total_iteration -= 10

    def aceptation_criteria(self, value_1, value_2, kind = 0):
        if(kind == 0):
            if self.optimization_problem.calcule_fitness(value_1)<self.optimization_problem.calcule_fitness(value_2):#sera que este no es igual al opt del otro codigo?
                self.factsol += 1
                return True
            else:
                self.infactsol += 1
                return False
        else:
            if self.optimization_problem.calcule_fitness(value_1)<self.optimization_problem.calcule_fitness(value_2):
                self.imprperc = 1 - self.optimization_problem.calcule_fitness(value_1)/(self.optimization_problem.calcule_fitness(value_2))
            else:
                self.termination_criterion()
            self.save_regression_info()

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
            poblation_values = self.modify_poblation(poblation_number,poblation_values,random_solution)
        return poblation_number,poblation_values

    def modify_poblation(self,poblation_number,poblation_values,random_solution):
        while(poblation_number < len(poblation_values)):
            poblation_values.pop()
        while(poblation_number > len(poblation_values)):
            poblation_values.append(random_solution())
        return poblation_values

    def save_regression_info(self):
        self.parameter_model['PercFactSol'].append(self.factsol/(self.factsol+self.infactsol))
        self.parameter_model['PercInfactSol'].append(self.infactsol/(self.factsol+self.infactsol))
        self.parameter_model['ImprPerc'].append(self.imprperc)

    def regression_model(self):
        X,Y,df = self.processing_data()
        regr = LinearRegression()
        regr.fit(X,Y)
        self.roulette[0]= regr.predict([[X.iloc[0]['PercFactSol'],X.iloc[0]['PercInfactSol']]])
        self.roulette[1]= regr.predict([[X.iloc[1]['PercFactSol'],X.iloc[1]['PercInfactSol']]])
        self.roulette[2]= regr.predict([[X.iloc[2]['PercFactSol'],X.iloc[2]['PercInfactSol']]])
        self.roulette[3]= regr.predict([[X.iloc[3]['PercFactSol'],X.iloc[3]['PercInfactSol']]])
        self.roulette[4]= regr.predict([[X.iloc[4]['PercFactSol'],X.iloc[4]['PercInfactSol']]])
        self.normalize(self.roulette)

    def processing_data(self):
        #y: posible fitness, x: % factibles , %infactibles, %mejora fitness, cant_poblacion
        aux_df = pd.DataFrame()
        df = pd.DataFrame(self.parameter_model,columns=['PercFactSol', 'PercInfactSol','ImprPerc'])
        df = df.replace([np.inf, -np.inf], np.nan).dropna(how='any')
        df = df.fillna(0)
        for i in range(5):
            max_row = df.iloc[df['ImprPerc'].idxmax()].to_frame().T
            df = df.drop(df.index[[df['ImprPerc'].idxmax()]])
            aux_df = pd.concat([max_row, aux_df], ignore_index=True)
            df2 = pd.DataFrame([[0]*df.shape[1]],columns=df.columns)
            df = df.append(df2, ignore_index=True)
        X = aux_df[['PercFactSol', 'PercInfactSol']]
        Y = aux_df['ImprPerc']
        return X,Y,df

    def normalize(self,roulette):
        roulette_sum = np.sum(np.absolute(roulette))
        for i in range(len(roulette)):
            with warnings.catch_warnings():
                warnings.filterwarnings('error')
                try:
                    roulette[i] = abs(roulette[i])/roulette_sum
                except Warning as e:
                    roulette[i] = 0
