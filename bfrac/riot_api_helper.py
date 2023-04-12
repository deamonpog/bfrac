class RiotAPIHelper:
    """
    Helper class containing static methods for calling common riot api endpoints.
    """
    lol_servers = ["br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "ph2", "ru", "sg2", "th2", "tr1",
                   "tw2", "vn2"]
    lol_continents = ["americas", "asia", "europe", "sea"]

    """
    The AMERICAS routing value serves NA, BR, LAN and LAS.
    The ASIA routing value serves KR and JP.
    The EUROPE routing value serves EUNE, EUW, TR and RU.
    The SEA routing value serves OCE, PH2, SG2, TH2, TW2 and VN2.
    """

    @staticmethod
    def url_summoner_by_name(in_region_server, in_summoner_name):
        return f"https://{in_region_server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{in_summoner_name}"

    @staticmethod
    def url_summoner_by_puuid(in_region_server, in_encrypted_puuid):
        return f"https://{in_region_server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{in_encrypted_puuid}"

    @staticmethod
    def url_match_list_by_summoner_puuid(in_region_continent, in_puuid):
        return f"https://{in_region_continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/{in_puuid}/ids"

    @staticmethod
    def url_match_info(in_region_continent, in_match_id):
        return f"https://{in_region_continent}.api.riotgames.com/lol/match/v5/matches/{in_match_id}"

    @staticmethod
    def url_match_timeline(in_region_continent, in_match_id):
        return f"https://{in_region_continent}.api.riotgames.com/lol/match/v5/matches/{in_match_id}/timeline"

    @staticmethod
    def get_summoner_by_name(in_riot_api_caller, in_region, in_summoner_name):
        url = RiotAPIHelper.url_summoner_by_name(in_region, in_summoner_name)
        return in_riot_api_caller.call_riot_api(url, {})

    @staticmethod
    def get_matches_list(in_riot_api_caller, in_region_continent, in_summoner_puuid, in_count,
                         in_type="", in_queue=None, in_start_time=0, in_end_time=0, in_start=0):
        """

        Parameters
        ----------
        in_riot_api_caller : RiotAPICaller
            A valid RiotAPICaller object that could be used to call the endpoint.
        in_region_continent : str
            One of region values from {"americas", "asia", "europe", "sea"}
            This is the region for this query.
        in_summoner_puuid : str
            PUUID of the summoner
        in_count : int
            Number of matches to download.
            "count" parameter in RiotAPI endpoint.
        in_type : str
            One of the values from {"ranked", "normal", "tourney", "tutorial"}
            Which type of matches to download.
            Default value is empty string ("") which downloads all matches without filtering.
            "type" parameter in RiotAPI endpoint.
        in_queue : int
            Queue ID given by RiotAPI.
            E.g. 420 is the ranked solo queue id
            "queue" parameter in RiotAPI endpoint.
        in_start_time : long
            "startTime" parameter in RiotAPI endpoint.
        in_end_time : long
            "endTime" parameter in RiotAPI endpoint.
        in_start : int
            "start" parameter in RiotAPI endpoint.

        Returns
        -------
        Object
        Match list dataset
        """
        url = RiotAPIHelper.url_match_list_by_summoner_puuid(in_region_continent, in_summoner_puuid)
        params = {"count": in_count, "start": in_start}
        if in_type:
            params["type"] = in_type
        if in_queue is not None:
            params["queue"] = in_type
        if in_start_time > 0:
            params["startTime"] = in_start_time
        if in_end_time > 0:
            params["endTime"] = in_end_time
        return in_riot_api_caller.call_riot_api(url, params)

    @staticmethod
    def get_match_info(in_riot_api_caller, in_region_continent, in_match_id):
        url = RiotAPIHelper.url_match_info(in_region_continent, in_match_id)
        return in_riot_api_caller.call_riot_api(url, {})

    @staticmethod
    def get_match_timeline(in_riot_api_caller, in_region_continent, in_match_id):
        url = RiotAPIHelper.url_match_timeline(in_region_continent, in_match_id)
        return in_riot_api_caller.call_riot_api(url, {})
