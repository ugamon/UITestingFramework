# encoding=utf-8

class HttpGet:

    def __init__(self):
       import local_config
       from requests import get

       self.GET = get
       self.URL = local_config.URL
       self.QUERY_STRING = local_config.QUERY_STRING
       self.CUSTOM_HEADERS = local_config.CUSTOM_HEADERS

    def get_request(self):
        return self.GET(self.URL)

    def get_request_querystring(self):
        return self.GET(self.URL,params=self.QUERY_STRING)

    def get_request_headers(self):
        return self.GET(self.URL, headers=self.CUSTOM_HEADERS)



