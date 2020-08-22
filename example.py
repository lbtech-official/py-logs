"""
Step #4: redirect stdout/stderr to a single file.
"""
import logging
# import sys
# import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)d-%(levelname)s-%(message)s',
    # handlers=[logging.StreamHandler(stream=sys.stdout)]  # force use STDOUT instead of STDERR
)

print('Print')  # Print uses sys.stdout by default

logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')

# time.sleep(60)  # for Linux demo to show Standart Streams (descriptors) in action


# Terminal commands (Unix/Linux):

# === ATTEMPT #1: ===
# By default, functions debug(), info(), warning(), error() and critical()
# are set to a destination of the console (sys.stderr)
# https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial

#   clear && :> example.log && python3 example.py > example.log && cat example.log

#   Console Output:

#   18468-DEBUG-Debug
#   18468-INFO-Info
#   18468-WARNING-Warning
#   18468-ERROR-Error
#   18468-CRITICAL-Critical

#   File output:
#   ───────┬───────────────────────
#          │ File: example.log
#   ───────┼───────────────────────
#      1   │ Print
#   ───────┴───────────────────────

# === ATTEMPT #2: ===
# Redirecting stdout and stderr using file descriptors.
# We also can use `>>` redirect as `filemode='a'` analog.
# Note that `Print` is beyond of log output (incorrect order).

#   clear && :> example.log && python3 example.py &> example.log && cat example.log

#   Console Output:
#   <empty>

#   File output:
#   ───────┬───────────────────────────
#          │ File: example.log
#   ───────┼───────────────────────────
#      1   │ 28457-DEBUG-Debug
#      2   │ 28457-INFO-Info
#      3   │ 28457-WARNING-Warning
#      4   │ 28457-ERROR-Error
#      5   │ 28457-CRITICAL-Critical
#      6   │ Print
#   ───────┴───────────────────────────

# === ATTEMPT #3: ===
# Using `handlers=[logging.StreamHandler(stream=sys.stdout)]` to log directly to
# stdout to resolve ordering problem.
# Note that `Print` and log output are displayed in the correct order now.

#   clear && :> example.log && python3 example.py &> example.log && cat example.log

#   Console Output:
#   <empty>

#   File output:
#   ───────┬───────────────────────────
#          │ File: example.log
#   ───────┼───────────────────────────
#      1   │ Print
#      2   │ 28457-INFO-Info
#      3   │ 28457-WARNING-Warning
#      4   │ 28457-ERROR-Error
#      5   │ 28457-CRITICAL-Critical
#      6   │ 28457-DEBUG-Debug
#   ───────┴───────────────────────────
