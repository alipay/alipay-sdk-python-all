#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdDeviceinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdDeviceinfoQueryResponse, self).__init__()
        self._device_info = None
        self._risk_info = None

    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        self._device_info = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdDeviceinfoQueryResponse, self).parse_response_content(response_content)
        if 'device_info' in response:
            self.device_info = response['device_info']
        if 'risk_info' in response:
            self.risk_info = response['risk_info']
