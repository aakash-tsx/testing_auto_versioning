import logging
import os
from logging.handlers import RotatingFileHandler

# Constants for log configuration
LOG_DIR = "logs"
LOG_FILE = "app.log"  # Fixed name for better rotation efficiency
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Create log directory if it doesn't exist
log_dir_path = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)


def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    Ensures the logger is set up only once.
    """
    if len(logging.getLogger().handlers) > 0:
        return  # Prevent duplicate logging setup

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define log format
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotating file handler
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler (INFO and above only)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# Configure the logger
configure_logger()
