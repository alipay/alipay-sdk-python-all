#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotWifiResultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotWifiResultQueryResponse, self).__init__()
        self._result_type = None
        self._ssid = None

    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def ssid(self):
        return self._ssid

    @ssid.setter
    def ssid(self, value):
        self._ssid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotWifiResultQueryResponse, self).parse_response_content(response_content)
        if 'result_type' in response:
            self.result_type = response['result_type']
        if 'ssid' in response:
            self.ssid = response['ssid']
