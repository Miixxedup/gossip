import json
import requests
from .config import *
from .gossip_querybuilder import GossipQueryBuilder

# Object to store the Gossip request
class GossipRequest():
    def __init__(self, args = None, endpoint= ENDPOINT):
        if args:
            self.endpoint = endpoint
            self.searchkey = args.s
            self.specific_field=args.f
            self.source=args.src
        else:
            self.endpoint = endpoint
            self.upload = args

    # Request the resource
    def search_request(self):
        query = GossipQueryBuilder.search_query_builder(self, self.searchkey, self.specific_field, self.source, self.endpoint)
        r = requests.get(query,
        headers={
            'Content-Type': 'application/json'
        })
        return r.json()
    
    # Stores a new value in Strapi
    def store_request(self):
        r = requests.post(f"{self.endpoint}/gossips",
            data = json.dumps({
                "indicator":f"{self.upload[0]}",
                "comment":f"{self.upload[1]}",
                "type":f"{self.upload[2]}"
            }),
            headers={
                'Content-Type': 'application/json'
            })
        print(r.status_code)