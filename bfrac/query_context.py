from riot_api_helper import RiotAPIHelper


class QueryContext:
    """
    Keeps track of context of the query so that multiple queries could be run without having to
    enter the same data again and again.
    """

    def __init__(self, in_riot_api_caller: RiotAPIHelper):
        self.riot_api_caller = None
        self.region_server = None
        self.region_continent = None
        self.summoner_encrypted_id = None
        self.summoner_account_id = None
        self.summoner_puuid = None
        self.summoner_name = None
        self.set_riot_api_caller(in_riot_api_caller)

    def set_riot_api_caller(self, in_riot_api_caller):
        self.riot_api_caller = in_riot_api_caller

    def set_region_server(self, in_region_server):
        self.region_server = in_region_server
        self.region_continent = RiotAPIHelper.LOL_SERVER_TO_CONTINENT[in_region_server]

    def get_summoner_by_name(self, in_summoner_name):
        self.summoner_name = in_summoner_name
        summoner_info = RiotAPIHelper.get_summoner_by_name(self.riot_api_caller, self.region_server, self.summoner_name)
        self.summoner_encrypted_id = summoner_info['id']
        self.summoner_account_id = summoner_info['accountId']
        self.summoner_puuid = summoner_info['puuid']
        self.summoner_name = summoner_info['name']
        return summoner_info

    def get_matches_list(self, in_count, in_type="", in_queue=None, in_start_time=0, in_end_time=0, in_start=0):
        matches_list = RiotAPIHelper.get_matches_list(self.riot_api_caller, self.region_continent, self.summoner_puuid,
                                                      in_count, in_type, in_queue, in_start_time, in_end_time, in_start)
        return matches_list

    def get_match_info(self, in_match_id):
        match_info = RiotAPIHelper.get_match_info(self.riot_api_caller, self.region_continent, in_match_id)
        return match_info
