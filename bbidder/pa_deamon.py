#!/usr/bin/env python3
from jsonrpcserver import dispatch
import sys
import time
import datetime
import zmq
import argparse
from bbidder.paceController import PacingController                         
from bbidder.utils.logger import logger
from bbidder.utils.config import Config
import time

def main():
    parser = argparse.ArgumentParser(description='Pacing Algorithm Deamon')
    parser.add_argument('--limit', default = Config.getParam('pacing','defaultlimit'))
    parser.add_argument('--reset-time', default=Config.getParam('pacing','defaultresettime'))
    args = parser.parse_args()
    pc = PacingController(args.limit, args.reset_time)
    
    # Start zmq socket
    context = zmq.Context(1)
    server = context.socket(zmq.REP)
    bind_address = Config.getParam('pacing','bindaddrserver')
    logger.info('Binding to %s' % bind_address)
    server.bind(bind_address)    

    # Populate rpc methods dict
    methods = {
        'pa_push_bid': pc.pa_push_bid,
        'pa_reset': pc.reset
    }
    stime = time.time()
    # Enter main loop
    try:
        logger.info('Entering main loop')
        while True:
            # reset campaigns bids count 
            # if reset time has been reached
            ctime = time.time()
            if ctime - stime > 1000:
                stime = ctime
                pc.reset()
                logger.info('pacing reset performed')
                
            request = server.recv_json()
            logger.info('main loop req {0}'.format(request))
            response = dispatch(methods, request)
            server.send_json(response)
    finally:
        logger.info('Cleaning up')
        server.close()
        context.term()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.info('Encoutered unhandled exception %s' % e)
        raise
