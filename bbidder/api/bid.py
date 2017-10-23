from bbidder.services.provider import BidProvider

def post(bid):
    return BidProvider().postBidHandler(bid)
