class GossipQueryBuilder():
    def __init__(self):
        pass

    def search_query_builder(self, search_key, specific_field, source, endpoint):
        return f"{endpoint}/gossips?{specific_field}={search_key}&type={source}"

    def store_query_builder(self):
        pass
