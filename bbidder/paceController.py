class PacingController:

    def __init__(self, limit=100, reset_time=1000, campaigns = {}):
        self.campaigns = campaigns
        self.limit = int(limit)
        self.reset_time = int(reset_time)
    def pa_push_bid(self, campaignid):
        
        if campaignid in self.campaigns:
             self.campaigns[campaignid] += 1
        else:
             self.campaigns.update({campaignid:int(1)})
                  
        if self.campaigns[campaignid] <= self.limit:
            return True
        else:
            return False
        
    def setLimit(self, limit):
        self.limit = limit    
        
    def reset(self):
        self.campaigns={k:0 for k in self.campaigns}
        return True