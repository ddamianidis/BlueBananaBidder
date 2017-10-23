#!/usr/bin/env python3
import json
import requests
from bbidder.utils.config import Config
from bbidder.utils.logger import logger

class Campaign:
    
    def __init__(self, id, name, price, adm, targetedCountries):
        self.id = id
        self.name = name
        self.price = price
        self.adm = adm
        self.targetedCountries = targetedCountries
        
       
class CampaignsFact:
    ID_KEY = Config.getParam('campaignresponse','id')
    NAME_KEY = Config.getParam('campaignresponse', 'name')
    PRICE_KEY = Config.getParam('campaignresponse', 'price')
    ADM_KEY = Config.getParam('campaignresponse', 'adm')
    TC_KEY = Config.getParam('campaignresponse', 'targetedcountries')
    host_url = Config.getParam('campaignrequest', 'hosturl')
    headers = {
                  'Content-Type': 'application/json'
                }
        
    def __init__(self):
        self.campaigns = self.get()
        self.filtered_campaigns = None
    
    def buildCampaigns(self, camp_data):
        campaigns_list = []
        for camp in camp_data:
            camp_inst = Campaign(camp[self.ID_KEY], camp[self.NAME_KEY],
                                 camp[self.PRICE_KEY], camp[self.ADM_KEY], camp[self.TC_KEY])
            campaigns_list.append(camp_inst)
        return campaigns_list
             
    def get(self):
        mock_data = Config.getMockedCampaigns()
        if not mock_data:
            response = requests.get(url = self.host_url, headers=self.headers)
            camp_data = response.json() 
            if response.status_code is not 200:
                logger.info('Campaign request failed with code:{0}'.format(response.status_code))
                raise BidderException ('Campaign request failed with code:{0}'.format(response.status_code))
        else:
            camp_data = mock_data
            
        self.campaigns = self.buildCampaigns(camp_data)                 
        return self.campaigns
    
    def setFilter(self, country_code):
        def filter_func(camp):
            return country_code in [ c for c in camp.targetedCountries]
    
        if self.campaigns:
            self.filtered_campaigns = list(filter(filter_func, self.campaigns))
            return self.filtered_campaigns 
        else:
            # log and raise exception     
            logger.info('No campaigns in pool')
            return None
        
    def getSorted(self, sort_key):
          
        if self.filtered_campaigns:
            return sorted(self.filtered_campaigns, key=lambda k: getattr(k, sort_key), reverse = True)   
        else:
            # log and raise exception     
            logger.info('No campaigns after filtering')
            return None    
    
    def getWinningCampaign(self, country_code, sort_key):    
        if self.setFilter(country_code):
            camps_sorted_by_price = self.getSorted(sort_key)
            return camps_sorted_by_price[0]
        else:
            logger.info('No winning campaign')
            return None 
        