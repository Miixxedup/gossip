class GossipItem():
    def __init__(self, blob, detailed = False):
        self.blob = blob
        self.detailed = detailed
    
    def show_results(self):
        # Get fields from blob
        if len(self.blob) == 0: 
            print("No results returned by endpoint")
            return 
        if 'statusCode' in self.blob and self.blob['statusCode'] != 200:
            print(self.blob['error'])
            return
        if self.detailed:
            for b in self.blob:
                print(b)
        else:
            for i in self.blob:
                print(f"*** {i['createdAt'][0:10]} || {i['indicator']} ||  {i['comment']} ***")
        
        return len(self.blob)