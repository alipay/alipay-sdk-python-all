#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskHideDeviceidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskHideDeviceidQueryResponse, self).__init__()
        self._deviceid = None

    @property
    def deviceid(self):
        return self._deviceid

    @deviceid.setter
    def deviceid(self, value):
        self._deviceid = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskHideDeviceidQueryResponse, self).parse_response_content(response_content)
        if 'deviceid' in response:
            self.deviceid = response['deviceid']
