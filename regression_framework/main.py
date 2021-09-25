import logging
from regression_framework.functions.sphere_function import Sphere_function
from regression_framework.functions.shifted_elliptic_function import Shifted_elliptic_function
from regression_framework.functions.shifted_rastrigin_function import Shifted_rastrigin_function
from regression_framework.functions.shifted_ackley_function import Shifted_ackley_function
from regression_framework.functions.one_separable_shifted_rotated_elliptic_function import One_separable_shifted_rotated_elliptic_function
from regression_framework.functions.one_separable_shifted_and_rotated_rastrigin_function import One_separable_shifted_and_rotated_rastrigin_function

from regression_framework.functions import list_functions
from regression_framework.regressions_models.multiple_lineal_model import Multiple_lineal_model
from regression_framework.regressions_models.bayesian_ridge_model import Bayesian_ridge_model
from regression_framework.regressions_models.elastic_net_model import Elastic_net_model
from regression_framework.regressions_models.elastic_net_cv_model import Elastic_net_cv_model
from regression_framework.regressions_models.ridge_model import Ridge_model
from regression_framework.regressions_models.lasso_model import Lasso_model
from regression_framework.admins.logistic_admin import Logistic_admin

from regression_framework.functions.extended_powell_singular_function import Extended_powell_singular_function
from regression_framework.functions.extended_rosenbrock_function import Extended_rosenbrock_function
from regression_framework.functions.linear_full_rank import Linear_full_rank
from regression_framework.functions.penalty_i_function import Penalty_I_function
from regression_framework.functions.variably_dimensioned_function import Variably_dimensioned_function


def create_admin():
    
    holi = Variably_dimensioned_function()
    print(holi.name)
    #Lasso_model(holi).run_model(100)

    #/home/pcontreras/prueba/runner.sh testConfig1 3 1234567 /home/pcontreras/prueba/instancias/f3   -- 0.1327
    # ['prueba.py', '-i', '/home/pcontreras/prueba/instancias/f3', '--seed', '1234567', 'testConfig1', '3', '1234567', '/home/pcontreras/prueba/instancias/f3', '--', '0.1327']


    admin = Logistic_admin(3,100,create_models(holi)) 
    return admin
    #return

def create_models(function):
    return [Bayesian_ridge_model(function),Elastic_net_model(function),Ridge_model(function),Lasso_model(function),Elastic_net_cv_model(function)]


def __main__():
    logging.info("Creating models")
    admin = create_admin()
    admin.run_admin()
