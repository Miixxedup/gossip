import json
import requests

# Object to store the Gossip request
class GossipRequest():
    def __init__(self,args ,endpoint= "http://localhost:1337"):
        self.endpoint = endpoint
        self.searchkey = args.s
        self.specific_field=args.f
        self.source=args.src

    # Request the resource
    def search_request(self):
        r = requests.get(f"{self.endpoint}/gossips?{self.specific_field}={self.searchkey}&type={self.source}",
        headers={
            'Content-Type': 'application/json'
        })
        return r.json()
    
    def store_request(self, indicator, comment):
        r = requests.post(f"{self.endpoint}/gossips",
        data = json.dumps({
            "indicator":f"{indicator}",
            "comment":f"{comment}"
        }),
        headers={
            'Content-Type': 'application/json'
        })
        return r.json()