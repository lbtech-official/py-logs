"""
Step #6: error handling.
"""
from math import sqrt
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


# === Handled exception #1 ===
try:
    1/0
except Exception:
    logger.error('Handled exception #1', exc_info=True)
    print('=' * 20)


# === Handled exception #2 ===
try:
    1/0
except Exception:
    logger.exception('Handled exception #2')
    print('=' * 20)


# === Unhandled exceptin #3 ===
sqrt(-1)


# clear && :> example.log && python3 example.py && cat example.log

# Console output:

# Print
# 2156 - DEBUG - Debug
# 2156 - INFO - Info
# 2156 - WARNING - Warning
# 2156 - ERROR - Handled exception #1
# Traceback (most recent call last):
#   File "example.py", line 37, in <module>
#     1/0
# ZeroDivisionError: division by zero
# ====================
# 2156 - ERROR - Handled exception #2
# Traceback (most recent call last):
#   File "example.py", line 45, in <module>
#     1/0
# ZeroDivisionError: division by zero
# ====================
# Traceback (most recent call last):
#   File "example.py", line 52, in <module>
#     sqrt(-1)
# ValueError: math domain error

# File output:
# ───────┬──────────────────────────────────────────────────────────────────────
#        │ File: example.log
# ───────┼──────────────────────────────────────────────────────────────────────
#    1   │ 2020-08-23 12:37:25,136 - __main__ - ERROR - Handled exception #1
#    2   │ Traceback (most recent call last):
#    3   │   File "example.py", line 37, in <module>
#    4   │     1/0
#    5   │ ZeroDivisionError: division by zero
#    6   │ 2020-08-23 12:37:25,136 - __main__ - ERROR - Handled exception #2
#    7   │ Traceback (most recent call last):
#    8   │   File "example.py", line 45, in <module>
#    9   │     1/0
#   10   │ ZeroDivisionError: division by zero
# ───────┴──────────────────────────────────────────────────────────────────────
