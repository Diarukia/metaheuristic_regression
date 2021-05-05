from regression_framework.functions.sphere_function import Sphere_function
from regression_framework.functions.schwefel_function_2_22 import Schwefel_function_2_22
from regression_framework.functions.schwefel_function_1_2 import Schwefel_function_1_2
from regression_framework.functions.generalized_rosenbrock_function import Generalized_rosenbrock_function
from regression_framework.functions.generalized_schwefel_function_2_26 import Generalized_schwefel_function_2_26
from regression_framework.functions.generalized_rastrigin_function import Generalized_rastrigin_function
from regression_framework.functions.ackley_function import Ackley_function
from regression_framework.functions.generalized_griewank_function import Generalized_griewank_function
from regression_framework.functions.generalized_penalized_function import Generalized_penalized_function
from regression_framework.functions.shekel_foxholes_function import Shekel_foxholes_function
from regression_framework.functions.six_hump_camel_back_function import Six_hump_camel_back_function
from regression_framework.functions.branin_function import Branin_function
from regression_framework.functions.goldstein_price_function import Goldstein_price_function
from regression_framework.functions.hartman_family_function_1 import Hartman_family_function_1
from regression_framework.functions.hartman_family_function_2 import Hartman_family_function_2
from regression_framework.functions.shifted_elliptic_function import Shifted_elliptic_function



def list_functions():
    return [Sphere_function(),Schwefel_function_2_22(),Schwefel_function_1_2(),Generalized_rosenbrock_function(),Generalized_schwefel_function_2_26()
           ,Generalized_rastrigin_function(),Ackley_function(),Generalized_griewank_function(),Generalized_penalized_function(),Shekel_foxholes_function()
           ,Six_hump_camel_back_function(),Branin_function(),Goldstein_price_function(),Hartman_family_function_1(),Hartman_family_function_2()
           ,Shifted_elliptic_function()]