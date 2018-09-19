#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityInfoAnalysisResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityInfoAnalysisResponse, self).__init__()
        self._risk_code = None
        self._risk_level = None

    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityInfoAnalysisResponse, self).parse_response_content(response_content)
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'risk_level' in response:
            self.risk_level = response['risk_level']
