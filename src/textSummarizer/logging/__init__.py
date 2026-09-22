import os 
import logging
import sys
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),# filehandler is used to write the logs to a file, in this case, running_logs.log
        logging.StreamHandler(sys.stdout) # to display the logs on the console, we use StreamHandler and pass sys.stdout to it. This will print the logs to the console as well as write them to the file.
    ]
)

logger = logging.getLogger("textSummarizerlogger") # we create a logger object and pass the name of the logger as an argument. This name will be used to identify the logger in the logs.