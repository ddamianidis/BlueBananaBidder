from flask import jsonify
import json
from bbidder.campaigns import CampaignsFact, Campaign
from connexion import NoContent
from bbidder.utils.config import Config
from bbidder.utils.exceptions import BidderException
from bbidder.utils.logger import logger
from bbidder.rpc_client import rpcClient
import zmq
from jsonrpcclient import Request
                            
class BidProvider():
    ID_REQ_KEY = Config.getParam('bidrequest', 'id')
    APP_REQ_KEY = Config.getParam('bidrequest', 'app')
    DEVICE_REQ_KEY = Config.getParam('bidrequest', 'device')
    GEO_REQ_KEY = Config.getParam('bidrequest', 'geo')
    COUNTRY_REQ_KEY = Config.getParam('bidrequest', 'country')
    ID_RESP_KEY = Config.getParam('bidresponse', 'id')
    BID_RESP_KEY = Config.getParam('bidresponse', 'bid')
    CAMPAIGNID_RESP_KEY = Config.getParam('bidresponse', 'campaignid')
    PRICE_RESP_KEY = Config.getParam('bidresponse', 'price')
    ADM_RESP_KEY = Config.getParam('bidresponse', 'adm')
    
    def __init__(self):
        pass
    
    def postBidHandler(self, bid):
        bid_id = bid[self.ID_REQ_KEY]
        bid_country = bid[self.DEVICE_REQ_KEY][self.GEO_REQ_KEY][self.COUNTRY_REQ_KEY] 
        try:
            wincamp = CampaignsFact().getWinningCampaign(bid_country, CampaignsFact.PRICE_KEY)
        except  BidderException as error:
            logger.info('Campaign request error: {0}'.format(error))
               
        if wincamp:
            pa_resp = {'campaignid':wincamp.id}
            pa_status = rpcClient('pa_push_bid', pa_resp).call()
            if pa_status:
                return {
                            self.ID_RESP_KEY: bid_id,
                            self.BID_RESP_KEY: {
                            self.CAMPAIGNID_RESP_KEY: wincamp.id,
                            self.PRICE_RESP_KEY: wincamp.price,
                            self.ADM_RESP_KEY: wincamp.adm
                            }
                        }
            else:
                return NoContent, 204
        else:
            return NoContent, 204
