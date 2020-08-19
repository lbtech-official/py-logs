import logging

# Print uses sys.stdout by default
# https://github.com/python/cpython/blob/2.7/Python/bltinmodule.c#L1580
print('Print')

# Logging provides a set of convenience functions for simple logging usage
logging.debug('Debug')
logging.info('Info')
# The default level is WARNING,
# which means that only events of this level and above will be tracked,
# unless the logging package is configured to do otherwise.
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')


# Output:

# Print
# WARNING:root:Warning
# ERROR:root:Error
# CRITICAL:root:Critical
