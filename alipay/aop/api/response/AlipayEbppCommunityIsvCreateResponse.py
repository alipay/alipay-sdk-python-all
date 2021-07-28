#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityIsvCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityIsvCreateResponse, self).__init__()
        self._isv_short_name = None

    @property
    def isv_short_name(self):
        return self._isv_short_name

    @isv_short_name.setter
    def isv_short_name(self, value):
        self._isv_short_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityIsvCreateResponse, self).parse_response_content(response_content)
        if 'isv_short_name' in response:
            self.isv_short_name = response['isv_short_name']
