"""
Structlog.
"""
from math import sqrt
from structlog_conf import get_logger


logger = get_logger(__name__)

nested = {
    'foo': 1,
    'bar': 'bar',
}
print('Print')
logger.debug('Dbg mes', code='De', nested=nested)
logger.info('Inf mes', code='In')
logger.warning('Wrng mes', code='Wa')
logger.critical('Crtcl mes', code='Cr')


def handled_error_func():
    """ Handled exception """
    log = logger.bind(code='Ex', bar='1')
    try:
        1/0
    except Exception:
        log.error('Handled exception', exc_info=True)
        print('=' * 10)


def unhandled_error_func():
    """ Unhandled exception """
    sqrt(-1)


handled_error_func()
unhandled_error_func()
