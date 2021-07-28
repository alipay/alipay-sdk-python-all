#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskAmlAnalyzeSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskAmlAnalyzeSubmitResponse, self).__init__()
        self._aml_decision = None
        self._aml_result_code = None
        self._biz_code = None
        self._request_id = None

    @property
    def aml_decision(self):
        return self._aml_decision

    @aml_decision.setter
    def aml_decision(self, value):
        self._aml_decision = value
    @property
    def aml_result_code(self):
        return self._aml_result_code

    @aml_result_code.setter
    def aml_result_code(self, value):
        self._aml_result_code = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskAmlAnalyzeSubmitResponse, self).parse_response_content(response_content)
        if 'aml_decision' in response:
            self.aml_decision = response['aml_decision']
        if 'aml_result_code' in response:
            self.aml_result_code = response['aml_result_code']
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'request_id' in response:
            self.request_id = response['request_id']
