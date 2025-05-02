import logging
from logging.handlers import RotatingFileHandler
import os


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str = "app_logger") -> logging.Logger:
    """ 
    Returns a logger with the given name, or the default "app_logger" if not provided.
    If the logger has not been created before, it is set up with a rotating file handler
    that writes to the app.log file within the logs directory. The file is limited to 100
    KiB in size, and up to 5 backup files are kept. The log format is "%(asctime)s - %(levelname)s - %(message)s".
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evita adicionar múltiplos handlers ao importar várias vezes
    if not logger.handlers:
        log_path = os.path.join(LOG_DIR, "app.log")
        handler = RotatingFileHandler(log_path, maxBytes=100_000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
