from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)


def index(request):
    print('Print `%s`' % __name__)
    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.critical('Critical')

    # Handled exception
    try:
        1/0
    except Exception:
        logger.exception('handled exception')
        print('=' * 20)

    return HttpResponse("Index")


def error(request):
    1/0
