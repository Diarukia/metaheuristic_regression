import logging
from regression_framework.functions import list_functions
from regression_framework.regressions_models.multiple_lineal_model import Multiple_lineal_model
from regression_framework.admins.logistic_admin import Logistic_admin

def create_admin():
    admin = Logistic_admin(10,100,[Multiple_lineal_model(list_functions()[0])])
    return admin


def __main__():
    logging.info("Creating models")
    admin = create_admin()
    admin.run_admin()
