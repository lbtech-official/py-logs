"""
Step #3: file output.
"""

import logging

# `filemode` specifies the mode to open the file, if filename is specified
# (if filemode is unspecified, it defaults to 'a').
logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)d-%(levelname)s-%(message)s',
    filename='example.log',
    filemode='w',  # overwrite
)

print('Print')  # Print uses sys.stdout by default

logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')


# Console Output:
# Print

# File output:
# File: example.log
# ───────┼──────────────────────────
#    1   │ 15263-DEBUG-Debug
#    2   │ 15263-INFO-Info
#    3   │ 15263-WARNING-Warning
#    4   │ 15263-ERROR-Error
#    5   │ 15263-CRITICAL-Critical
