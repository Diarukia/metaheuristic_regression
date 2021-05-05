import logging
from regression_framework.functions import list_functions
from regression_framework.regressions_models.multiple_lineal_model import Multiple_lineal_model
from regression_framework.regressions_models.bayesian_ridge_model import Bayesian_ridge_model
from regression_framework.regressions_models.elastic_net_model import Elastic_net_model
from regression_framework.regressions_models.elastic_net_cv_model import Elastic_net_cv_model
from regression_framework.regressions_models.ridge_model import Ridge_model
from regression_framework.regressions_models.lasso_model import Lasso_model
from regression_framework.admins.logistic_admin import Logistic_admin

def create_admin():
    print(list_functions()[1].name)
    admin = Logistic_admin(3,100,create_models(list_functions()[1]))
    return admin

def create_models(function):
    return [Bayesian_ridge_model(function),Elastic_net_model(function),Ridge_model(function),Lasso_model(function),Elastic_net_cv_model(function)]


def __main__():
    logging.info("Creating models")
    admin = create_admin()
    admin.run_admin()
