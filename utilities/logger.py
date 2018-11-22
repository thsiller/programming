import logging


def init_logging(filename=None, log_level=None):
    '''
    Adds a stream handler to the root logger and adds a file handler if `filename` is given.
    :param filename: Set a full path to a file if you want to add a file handler to the root logger
    :param log_level: Set this to 'DEBUG', 'INFO', 'WARNING' or 'ERROR' if you want to switch to the
    corresponding log level. Default log level is 'DEBUG'.
    :return: None
    '''
    if log_level is None:
        log_level = 'DEBUG'

    rootlogger = logging.getLogger()
    level = logging.getLevelName(log_level)
    rootlogger.setLevel(level)

    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s - %(message)s]')

    if filename is not None:
        fh = logging.FileHandler(filename)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        rootlogger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    rootlogger.addHandler(ch)


def log(func):
    logger = logging.getLogger(func.__name__)

    def wrapper(*args, **kwargs):
        logger.debug('call %s(signature = %s, kwargs = %s)' % (func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        logger.info('returning %s' % result)
        return result
    return wrapper


def method_log(func):
    logger = logging.getLogger(__name__)

    def wrapper(*args, **kwargs):
        obj = args[0]
        if obj.__class__.__name__ == '_ScenarioCacheProxy':
            name = '_ScenarioCacheProxy(%s).%s' % (obj._gen.__class__.__name__, func.__name__)
        elif obj.__class__.__name__ == '_BalanceSheetItemProxy':
            name = '_BalanceSheetItemProxy(%s).%s' % (obj._bsi.__class__.__name__, func.__name__)
        else:
            name = '%s.%s' % (obj.__class__.__name__, func.__name__)
        logger.debug('enter ' + name)
        result = func(*args, **kwargs)
        logger.debug('exit  ' + name)
        return result
    return wrapper
