# -*- coding: utf-8 -*-

from config import PROXY_ADDRESS, PROXY_USERNAME, PROXY_PASSWORD

from w3lib.http import basic_auth_header


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = PROXY_ADDRESS

        if PROXY_USERNAME and PROXY_PASSWORD:
            request.headers['Proxy-Authorization'] = basic_auth_header(PROXY_USERNAME, PROXY_PASSWORD)