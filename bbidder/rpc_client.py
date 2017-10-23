import zmq
from jsonrpcclient import Request
from bbidder.utils.config import Config
from bbidder.utils.exceptions import BidderException
from bbidder.utils.logger import logger

def rpc_call(method_name, **kwargs):
        bind_address = Config.getParam('pacing','bindaddrclient')
        request_timeout = int(Config.getParam('pacing','requesttimeout')) 
        context = zmq.Context(1)
        client = context.socket(zmq.REQ)
        logger.debug('bind adress is %s' %bind_address)
        client.connect(bind_address)
    
        poll = zmq.Poller()
        poll.register(client, zmq.POLLIN)
    
        request = Request(method_name, **kwargs)
        client.send_json(request)
    
        socks = dict(poll.poll(request_timeout))
        try:
            if socks.get(client) == zmq.POLLIN:
                reply = client.recv_json()
                logger.debug('reply from client {0}'.format(reply))
                return reply['result']
                
            else:
                return False
                #print("E: No response from server, closing...")
        finally:
            client.setsockopt(zmq.LINGER, 0)
            client.close()
            poll.unregister(client)
            context.term()

class rpcClient():
    
    def __init__(self, method, params):
        self.method = method
        self.params = params
        
    def call(self):
        return rpc_call(self.method, **self.params)
        
             