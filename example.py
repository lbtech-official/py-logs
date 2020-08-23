"""
Step #7: configuration over yaml.
"""
from math import sqrt
import logging
import logging.config
import yaml  # pip install pyyaml

# Load yaml config
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

# Custom logger
logger = logging.getLogger(__name__)

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
