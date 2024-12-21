import os
import logging
import sys
from utils.utilsfns import open_and_read_pdf
from config import data_dir

def data_preparation(data_dir, logger):
    logger.info("inside data_preparation.py")
    # Add the root directory to Python's path
    sys.path.append(os.path.abspath(".."))
    files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]

    if not files:
        logger.error("Data folder not found!")
        exit()
    
    logger.info("Data folder found.")
    filepath = data_dir + "/" + files[0]
    print(filepath)
    pages_and_texts = open_and_read_pdf(pdf_path=filepath)
    logger.info("Data converted into text.")
    logger.info("exiting data_preparation.py")
    return pages_and_texts