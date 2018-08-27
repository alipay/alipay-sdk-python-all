#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskCustomerriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskCustomerriskQueryResponse, self).__init__()
        self._risk_result = None
        self._risk_result_desc = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        self._risk_result = value
    @property
    def risk_result_desc(self):
        return self._risk_result_desc

    @risk_result_desc.setter
    def risk_result_desc(self, value):
        self._risk_result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskCustomerriskQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
        if 'risk_result_desc' in response:
            self.risk_result_desc = response['risk_result_desc']
