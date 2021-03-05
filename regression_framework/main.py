import logging
from regression_framework.functions import list_functions


def __main__():
    logging.info("Creating models")
    print(list_functions()[0].calcule_fitness(1.5))