import logging, inspect
import datetime as dt
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'util'))
from term_color import bcolors


def events_logger(file_basename: str, message: str, log_level_file_handler: int, log_level_for_console: int):
    """
    Python has six log levels with each one assigned a specific integer indicating the severity of the log:
    NOTSET=0
    DEBUG=10
    INFO=20
    WARN=30
    ERROR=40
    CRITICAL=50
"""
    func = inspect.currentframe().f_back.f_code
    
    today = dt.date.today()
    log_file_name = f"{today.day:02d}-{today.month:02d}-{today.year}.log"
    Ydl_Logger_file_name = f"Ydl_Logger-{today.day:02d}-{today.month:02d}-{today.year}.log"
                        
    logger = logging.getLogger(file_basename)

    stdout_handler = logging.StreamHandler() #  StreamHandler sends logs to console

    if "Ydl_Logger" in message.split():
        file_handler = logging.FileHandler(f'../logs/{Ydl_Logger_file_name}') # sends logs to disk files.
    else:
        file_handler = logging.FileHandler(f'../logs/{log_file_name}') # sends logs to disk files.
    
    # level  
    stdout_handler.setLevel(log_level_for_console)
    file_handler.setLevel(log_level_file_handler)

    # format
    formatter = logging.Formatter("%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s")
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)

    
    logger.setLevel(logging.DEBUG)

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    file_info = f'{func.co_filename} | { func.co_name} {bcolors.ENDC}'
    # Emit log message
    logger.debug(f" {bcolors.OKBLUE}  An debug:   {message} | {file_info}")
    logger.info(f" {bcolors.OKGREEN}  An info:  {file_info}  ")
    logger.warning(f"{bcolors.WARNING}A warning:  {message} | {file_info}")
    logger.error(f" {bcolors.FAIL}    An error:   {message} | {file_info}")
    logger.critical(f" {bcolors.FAIL} A critical: {message} | {file_info}")

