# Download PDF file
import os
from config import data_dir, min_token_length, save_path, model_name, device
import sys
from loguru import logger
import tqdm
import re
from sentence_transformers import SentenceTransformer
import pandas as pd
from components.data_preparation import data_preparation
from components.chunking_and_tolenization import chunking_and_tokenization
from components.embedding_generation import generate_embeddings



def train(logger):
    logger.info("Inside training_pipeline.py")

    # step 1: data preparation
    pages_and_texts = data_preparation(data_dir, logger)
    logger.info("data preparation done")

    # Step 2: Tokenize and chunk
    pages_and_chunks = chunking_and_tokenization(pages_and_texts, logger)
    logger.info("chunking and tokenization done")

    
    # Step 3: embed and save
    generate_embeddings(pages_and_chunks,min_token_length, model_name, device, logger)
    logger.info("embedding generation done")


    logger.info("Training pipeline completed.")