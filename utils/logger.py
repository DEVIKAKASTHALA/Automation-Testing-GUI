import logging
from pathlib import Path
from config.config import Config

def setup_logger(name=__name__, level=None):
    \"\"\"Setup logger with file and console handlers\"\"\"
    logger = logging.getLogger(name)
    logger.setLevel(level or Config.LOG_LEVEL)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler
    Config.LOG_FILE.parent.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(Config.LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger