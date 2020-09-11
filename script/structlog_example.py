"""
Structlog.
"""
from math import sqrt
import structlog
import logging
import logging.config
import yaml
from structlog.stdlib import LoggerFactory

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)


structlog.configure(logger_factory=LoggerFactory())

logger = structlog.get_logger()

nested = {
    'foo': 1,
    'bar': 'bar',
}
print('Print')
logger.debug('Dbg mes', extra_code='De', nested=nested)
logger.info('Inf mes', extra_code='In')
logger.warning('Wrng mes', extra_code='Wa')
logger.critical('Crtcl mes', extra_code='Cr')


def handled_error_func():
    # Handled exception
    log = logger.bind(extra_code='Ex', bar='1')
    try:
        1/0
    except Exception:
        log.error('Handled exception', exc_info=True)
        print('=' * 10)


def unhandled_error_func():
    # Unhandled exception
    sqrt(-1)


handled_error_func()
unhandled_error_func()
