"""
Step #2: basic config.
"""

import logging

# The call to basicConfig() should come before any calls
# to debug(), info() etc.
# As it’s intended as a one-off simple configuration facility,
# only the first call will actually do anything:
# subsequent calls are effectively no-ops.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)d-%(levelname)s-%(message)s',
)

print('Print')  # Print uses sys.stdout by default

logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')


# Output:

# Print
# 14733-DEBUG-Debug
# 14733-INFO-Info
# 14733-WARNING-Warning
# 14733-ERROR-Error
# 14733-CRITICAL-Critical
