#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPaiPartnerResultGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPaiPartnerResultGetResponse, self).__init__()
        self._data = None
        self._oauth_token = None
        self._route_method = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def oauth_token(self):
        return self._oauth_token

    @oauth_token.setter
    def oauth_token(self, value):
        self._oauth_token = value
    @property
    def route_method(self):
        return self._route_method

    @route_method.setter
    def route_method(self, value):
        self._route_method = value

    def parse_response_content(self, response_content):
        response = super(AlipayPaiPartnerResultGetResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'oauth_token' in response:
            self.oauth_token = response['oauth_token']
        if 'route_method' in response:
            self.route_method = response['route_method']
