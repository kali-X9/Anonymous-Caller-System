import logging
from logging.handlers import RotatingFileHandler
import os
from src.config import config

def setup_logger(name="AnonymousCaller"):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config["logging"]["level"]))

    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    os.makedirs(os.path.dirname(config["logging"]["log_file"]), exist_ok=True)
    file_handler = RotatingFileHandler(
        config["logging"]["log_file"],
        maxBytes=config["logging"]["max_bytes"],
        backupCount=config["logging"]["backup_count"]
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
