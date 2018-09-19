#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskReconfirmRiskidentifyCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskReconfirmRiskidentifyCertifyResponse, self).__init__()
        self._extend_info = None
        self._has_risk = None
        self._identify_id = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def identify_id(self):
        return self._identify_id

    @identify_id.setter
    def identify_id(self, value):
        self._identify_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskReconfirmRiskidentifyCertifyResponse, self).parse_response_content(response_content)
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
        if 'identify_id' in response:
            self.identify_id = response['identify_id']
