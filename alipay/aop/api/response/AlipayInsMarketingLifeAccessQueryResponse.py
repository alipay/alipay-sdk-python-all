#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingLifeAccessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingLifeAccessQueryResponse, self).__init__()
        self._access = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingLifeAccessQueryResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
