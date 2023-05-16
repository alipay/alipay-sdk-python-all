#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasInsuranceAccidentriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasInsuranceAccidentriskQueryResponse, self).__init__()
        self._found = None
        self._risk_result = None

    @property
    def found(self):
        return self._found

    @found.setter
    def found(self, value):
        self._found = value
    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        self._risk_result = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasInsuranceAccidentriskQueryResponse, self).parse_response_content(response_content)
        if 'found' in response:
            self.found = response['found']
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
