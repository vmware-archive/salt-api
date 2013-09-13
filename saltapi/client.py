'''
The main entry point for salt-api
'''
# Import python libs
import logging
import multiprocessing

# Import salt-api libs
import saltapi.loader

logger = logging.getLogger(__name__)

class SaltAPIClient(object):
    '''
    '''
    def __init__(self, opts):
        self.opts = opts

    def run(self):
        '''
        Load and start all available api modules
        '''
        netapi = saltapi.loader.netapi(self.opts)
        for fun in netapi:
            if fun.endswith('.start'):
                logger.info("Starting '{0}' api module".format(fun))
                multiprocessing.Process(target=netapi[fun]).start()
