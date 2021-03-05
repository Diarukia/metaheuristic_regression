from regression_framework.functions.base_function import Base_function

class Schwefel_function_2_22(Base_function):
    def __init__(self,name = 'Schwefel_function_2_22',lower_bound = -10,upper_bound = 10,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,value):
        x = np.asarray_chkfinite(value)
        return sum(abs(x))+prod(abs(x))

    def random_solution(self):
        randomSolution = random.random()*(2*self.upper_bound) - self.lower_bound
        return randomSolution