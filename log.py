import logging


logging.basicConfig(level=logging.DEBUG)  # or logger.setLevel(logging.DEBUG)
# THIS LINE MEANS LOGGER MUST SHOW THIS LEVEL AND HIGHER

logger = logging.getLogger()
# logger.disabled = True

logger.debug('This is to help with debugging') # 10
logger.info('This is just for information') # 20
logger.log(logging.INFO, "This is just for information")
logger.warning('This is a warning!') # 30
logging.warning('This is a warning!') # 30
logger.error('This should be used with something unexpected') # 40
logger.critical('Something serious') # 50

try:
    x = 1 / 0
except:
    logging.exception('an exception message')
    #logger.exception('an exception message')

print(logger.getEffectiveLevel())
print(logger.isEnabledFor(level=logging.NOTSET))
print(logger.isEnabledFor(level=logging.DEBUG))



logger = logging.getLogger()
print('Root logger:', logger)
logger1 = logging.getLogger('my logger')
print('Named logger:', logger1)
logger2 = logging.getLogger(__name__)
print('Module logger:', logger2)


logger.warning('%s is set to %d', 'count', 42)

# set handler and formatter---------------------------------------------
file_handler = logging.FileHandler('detailed.log')

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s',
                              datefmt='%m-%d-%Y %I:%M:%S|%p')
# mongh day year level name fname message

file_handler.setFormatter(formatter)
# Add the handler to the Logger
logger.addHandler(file_handler)
logger.info('Starting')

#filters-------------------------------------------------
class MyFilter(logging.Filter):
    def filter(self, record):
        if 'John' in record.msg:
            return False
        else:
            return True
logging.basicConfig(format='%(asctime)s %(message)s',
level=logging.DEBUG)
logger = logging.getLogger()
logger.addFilter(MyFilter())
logger.debug('This is to help with debugging')
logger.info('This is information on John')
