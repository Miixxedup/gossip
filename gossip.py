from gossip_helpers.gossip_formatter import GossipItem
from gossip_helpers.gossip_request import GossipRequest
import argparse


# Main flow
# - User enters variables and starts script.
# - GossIP requests a resource with some variables via Strapi
# - Strapi talks to MongoDB
# - Answer is return by MongoDB via Strapi
# - (Optional) Strapi does some magic
# - GossIP receives the answer
# - (Optional) Gossip does some magic
# - Answer is returned in CLI


# Parser section for the CLI
parser = argparse.ArgumentParser()
parser.add_argument('-s', help= "The indicator to search")
parser.add_argument('-f', default='indicator', help= "Search in a specific fied")
parser.add_argument('-u', help= "Upload supplied json blob to server")
parser.add_argument('-src', help= "Only select from a list of specified sources" ) #TODO implement functionality.
parser.add_argument('-d', action= 'store_true',help= "Return detailed results")
args = parser.parse_args()

# Main Logic flow
# Collect results from server
if args.s:
    GossipItem(GossipRequest(args).search_request(), detailed=args.d).show_results()
elif args.u:
    GossipItem(GossipRequest(args).search_request(), detailed=args.d).show_results()
else:
    print("Use gossip -h for help")
# Store results to server