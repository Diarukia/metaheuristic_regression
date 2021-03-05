from abc import ABC, abstractmethod

class Metaheuristic_poblation_base(ABC):
    def __init__(self,calcule_fitness,random_solution,poblation_number,poblation_values,aceptation_criteria,roulette_function,best_value = None):
        self.calcule_fitness = calcule_fitness
        self.poblation_number = poblation_number
        self.poblation_values = poblation_values
        self.aceptation_criteria = aceptation_criteria
        self.random_solution = random_solution
        self.roulette_function = roulette_function

    @abstractmethod
    def run_metaheuristic(self,number_poblation,poblation_values):
        pass

    def random_fill(self,poblation_number,poblation_values):
        if not a :
            for i in range(poblation_values):
                poblation_values.append(self.random_solution)
        return poblation_number