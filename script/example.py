"""
Step #8: Docker logs.
"""
import logging
import logging.config
import yaml
# import time
from math import sqrt

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

print('Print')
logger.debug('Debug', extra={'extra_code': 'De'})
logger.info('Info', extra={'extra_code': 'In'})
logger.warning('Warning', extra={'extra_code': 'Wa'})
logger.critical('Critical', extra={'extra_code': 'Cr'})

# Handled exception
try:
    1/0
except Exception:
    logger.error('Handled exception', extra={'extra_code': 'Ex'}, exc_info=True)

# Unhandled exception
sqrt(-1)  # !Uncomment to see that unhandled exceptions will appear in STDERR

# time.sleep(60)  # !Timeout to capture `docker logs` command in realtime
