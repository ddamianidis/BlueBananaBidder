#!/usr/bin/env python3
import connexion
from connexion.resolver import RestyResolver
from bbidder.utils.logger import logger


def main():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('bluebananabidder.yaml', resolver=RestyResolver('bbidder.api'))
    application = app.app

    # run our standalone server
    logger.info('Starting BlueBanana\'s Bidder ...')
    app.run(port=5000, server='gevent')

if __name__ == '__main__':
    main()
