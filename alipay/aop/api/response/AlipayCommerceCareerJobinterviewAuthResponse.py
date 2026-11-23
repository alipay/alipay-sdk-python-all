#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCareerJobinterviewAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerJobinterviewAuthResponse, self).__init__()
        self._ctoken = None
        self._expire_time = None

    @property
    def ctoken(self):
        return self._ctoken

    @ctoken.setter
    def ctoken(self, value):
        self._ctoken = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerJobinterviewAuthResponse, self).parse_response_content(response_content)
        if 'ctoken' in response:
            self.ctoken = response['ctoken']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
