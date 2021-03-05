from regression_framework.utils import setup_logging
from regression_framework.main import __main__
import logging

if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the regression framework")
    __main__()

