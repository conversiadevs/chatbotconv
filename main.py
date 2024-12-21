from config import mode
from loguru import logger
from datetime import datetime
from pipelines.training_pipeline import train

# Generate a logging filename with the current time
log_filename = f"logs/training_pipeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logger.add(log_filename, rotation="1 MB", level="INFO")


if(mode == "training"):
    logger.info("Training")
    train(logger)


if(mode == "inference"):
    pass