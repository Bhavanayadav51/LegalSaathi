import logging
import os


def setup_logger(name: str):

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("logs/app.log")

    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger