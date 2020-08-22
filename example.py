"""
Step #5: different handlers.
"""
import logging

# Custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # remember to configure top-level logging level

# Configure handlers
# Stream
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter('%(process)d - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_formatter)
# File
file_handler = logging.FileHandler(filename='example.log')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Configure logger with two handlers
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

print('Print')  # Print uses sys.stdout by default

# Using configured logger instance
logger.debug('Debug')
logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')


# clear && :> example.log && python3 example.py && cat example.log

# Console Output:
# Print
# 34360 - DEBUG - Debug
# 34360 - INFO - Info
# 34360 - WARNING - Warning
# 34360 - ERROR - Error
# 34360 - CRITICAL - Critical

# File output:
# ───────┬─────────────────────────────────────────────────────────────
#        │ File: example.log
# ───────┼─────────────────────────────────────────────────────────────
#    1   │ 2020-08-22 22:34:45,802 - __main__ - ERROR - Error
#    2   │ 2020-08-22 22:34:45,802 - __main__ - CRITICAL - Critical
# ───────┴─────────────────────────────────────────────────────────────
