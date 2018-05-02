# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .search_results_answer import SearchResultsAnswer


class TimeZone(SearchResultsAnswer):
    """Defines the data and time of one or more geographic locations.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries:
     list[~azure.cognitiveservices.search.websearch.models.Query]
    :ivar query_context:
    :vartype query_context:
     ~azure.cognitiveservices.search.websearch.models.QueryContext
    :ivar total_estimated_matches: The estimated number of webpages that are
     relevant to the query. Use this number along with the count and offset
     query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    :param primary_city_time: Required. The data and time, in UTC, of the
     geographic location specified in the query. If the query specified a
     specific geographic location (for example, a city), this object contains
     the name of the geographic location and the current date and time of the
     location, in UTC. If the query specified a general geographic location,
     such as a state or country, this object contains the date and time of the
     primary city or state found in the specified state or country. If the
     location contains additional time zones, the otherCityTimes field contains
     the data and time of cities or states located in the other time zones.
    :type primary_city_time:
     ~azure.cognitiveservices.search.websearch.models.TimeZoneTimeZoneInformation
    :ivar other_city_times: A list of dates and times of nearby time zones.
    :vartype other_city_times:
     list[~azure.cognitiveservices.search.websearch.models.TimeZoneTimeZoneInformation]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'query_context': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'is_family_friendly': {'readonly': True},
        'primary_city_time': {'required': True},
        'other_city_times': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
        'primary_city_time': {'key': 'primaryCityTime', 'type': 'TimeZoneTimeZoneInformation'},
        'other_city_times': {'key': 'otherCityTimes', 'type': '[TimeZoneTimeZoneInformation]'},
    }

    def __init__(self, *, primary_city_time, **kwargs) -> None:
        super(TimeZone, self).__init__(, **kwargs)
        self.primary_city_time = primary_city_time
        self.other_city_times = None
        self._type = 'TimeZone'
