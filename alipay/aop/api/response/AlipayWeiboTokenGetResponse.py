#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayWeiboTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayWeiboTokenGetResponse, self).__init__()
        self._access_token = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayWeiboTokenGetResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
