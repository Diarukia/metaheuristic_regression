import logging
import sys

def setup_logging():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO , filename='framework.log')

