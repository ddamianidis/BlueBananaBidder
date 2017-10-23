import unittest
import json
import requests
from bbidder.rpc_client import rpcClient

class BlueBananaAPITestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        rpcClient('pa_reset', {}).call()
        #pass
    
    #@unittest.skip('just skip')    
    def test_post_bid_1_with_body(self):
        reuest_body = """
              {
                "id": "e7fe51ce4f6376876353ff0961c2cb0d",
                "app": {
                  "id": "e7fe51ce-4f63-7687-6353-ff0961c2cb0d",
                  "name": "Morecast Weather"
                },
                "device": {
                  "os": "Android",
                  "geo": {
                    "country": "USA",
                    "lat": 0,
                    "lon": 0
                  }
                }
              }
            """
            
        response_body_expected = {
                  'id': 'e7fe51ce4f6376876353ff0961c2cb0d',
                  'bid': {
                            'campaignId': '5a3dce46',
                            'price': 1.23,
                            'adm': '<a href=\"http://example.com/click/qbFCjzXR9rkf8qa4\"><img src=\"http://assets.example.com/ad_assets/files/000/000/002/original/banner_300_250.png\" height=\"250\" width=\"300\" alt=\"\"/></a><img src=\"http://example.com/win/qbFCjzXR9rkf8qa4\" height=\"1\" width=\"1\" alt=\"\"/>\r\n'
                        }
                }
            
            
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.post(url = 'http://127.0.0.1:5000/bid', 
                                      data = reuest_body, headers = headers)
            
        self.assertEqual(response.status_code, 200, 'correct response status code')
        self.assertEqual(response.json(), response_body_expected, 'correct response body')
    
    #@unittest.skip('just skip')    
    def test_post_bid_2_without_body(self):
        reuest_body = """
              {
                  "id": "e7fe51ce4f6376876353ff0961c2cb0d",
                  "app": {
                    "id": "e7fe51ce-4f63-7687-6353-ff0961c2cb0d",
                    "name": "Morecast Weather"
                  },
                  "device": {
                    "os": "Android",
                    "geo": {
                      "country": "CYP",
                      "lat": 0,
                      "lon": 0
                    }
                  }
                }
            """         
            
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.post(url = 'http://127.0.0.1:5000/bid', 
                                      data = reuest_body, headers = headers)
             
        self.assertEqual(response.status_code, 204, 'correct response status code')
        self.assertEqual(response.text, '', 'correct response body')

    #@unittest.skip('just skip')    
    def test_post_bid_3_reach_pacing_limit(self):
        reuest_body = """
              {
                "id": "e7fe51ce4f6376876353ff0961c2cb0d",
                "app": {
                  "id": "e7fe51ce-4f63-7687-6353-ff0961c2cb0d",
                  "name": "Morecast Weather"
                },
                "device": {
                  "os": "Android",
                  "geo": {
                    "country": "USA",
                    "lat": 0,
                    "lon": 0
                  }
                }
              }
            """         
            
        headers = {
          'Content-Type': 'application/json'
        }
        
        for times in range(3):
            response = requests.post(url = 'http://127.0.0.1:5000/bid', 
                                      data = reuest_body, headers = headers)
             
        self.assertEqual(response.status_code, 204, 'correct response status code')
        self.assertEqual(response.text, '', 'correct response body')
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlueBananaAPITestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)