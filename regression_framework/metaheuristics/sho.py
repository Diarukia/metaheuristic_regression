from regression_framework.metaheuristics.metaheuristic_base import Metaheuristic_poblation_base

class Sho(Metaheuristic_poblation_base):
    def __init__(self,calcule_fitness,aceptation_criteria,h,poblation_number,poblation_values = list()):
        super().__init__(calcule_fitness,random_solution,poblation_number,poblation_values,aceptation_criteria,roulette_function)
        self.h = h
        self.current_iterations = current_iterations
    
    def run_metaheuristic(self,poblation_number,poblation_values,number_iterations):
        poblation_values= self.random_fill(poblation_number,poblation_values)
        e = 2*self.random_solution()*self.h-self.h
        b=2*self.random_solution()
        optimal_solutions = list() # ch
        best_solution_current = poblation_values[0]
        best_fitness_current = poblation_values[0]

        while(current_iterations < number_iterations):
            poblation_number,poblation_values = self.roulette_function(poblation_number,poblation_values,current_iterations,self.random_solution)

            for i in range(len(poblation_number)):
                pk = poblation_values[0]
                nuevaRana=best_solution_current-(e*((b*best_solution_current)-pk)) # 10 equation
                pk = nuevaRana

                if(self.aceptation_criteria(pk,poblation_values[i]) == False):
                    pk = poblation_values[i]
                ch.append(pk)

            for i in range(len(ch)):
                pk = poblation_values[0]
                actualrana=ch[i]
                atake=actualrana / len(ch)
                pk=atake
                if(self.aceptation_criteria(pk,ch[i]) == True)
                    poblation_values[i]=pk
                else:
                    poblation_values[i]=ch[i]
        return poblation_values