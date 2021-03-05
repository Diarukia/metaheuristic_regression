from regression_framework.metaheuristics.metaheuristic_base import Metaheuristic_poblation_base

class Sho(Metaheuristic_poblation_base):
    def __init__(self,calcule_fitness,aceptation_criteria,h,poblation_number,random_solution,roulette_function,poblation_values = list()):
        super().__init__(calcule_fitness,random_solution,poblation_number,poblation_values,aceptation_criteria,roulette_function)
        self.h = h
        self.current_iterations = 0
    
    def run_metaheuristic(self,poblation_number,poblation_values,number_iterations = 100):
        poblation_values= self.random_fill(poblation_number,poblation_values)
        poblation_values.sort()
        e = 2*self.random_solution()*self.h-self.h
        b=2*self.random_solution()
        optimal_solutions = list() # ch
        best_solution_current = poblation_values[0]
        best_fitness_current = poblation_values[0]
        while(self.current_iterations < number_iterations):
            poblation_number,poblation_values = self.roulette_function(poblation_number,poblation_values,self.current_iterations,self.random_solution)

            for i in range(poblation_number):
                pk = poblation_values[0]
                nuevaRana=best_solution_current-(e*((b*best_solution_current)-pk)) # 10 equation
                pk = nuevaRana

                if(self.aceptation_criteria(pk,poblation_values[i]) == False):
                    pk = poblation_values[i]
                optimal_solutions.append(pk)
            for i in range(len(optimal_solutions)):
                atake = 0
                pk = poblation_values[0]
                actualrana=optimal_solutions[i]
                atake=actualrana / len(optimal_solutions)
                pk=atake
                if(self.aceptation_criteria(pk,optimal_solutions[i]) == True):
                    poblation_values[i]=pk
                else:
                    poblation_values[i]=optimal_solutions[i]
            self.h = self.h - (self.current_iterations / number_iterations)
            e = 2*self.random_solution()*self.h-self.h
            b=2*self.random_solution()
            poblation_values.sort()
            if(self.aceptation_criteria(poblation_values[0],best_fitness_current,1) == True):
                best_solution_current = poblation_values[0]
                best_fitness_current = poblation_values[0]
            self.current_iterations += 1
            optimal_solutions = list()
        return poblation_values