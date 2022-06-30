#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GravityParam import GravityParam
from alipay.aop.api.domain.SecGravityServiceHeader import SecGravityServiceHeader
from alipay.aop.api.domain.GravityRiskResult import GravityRiskResult


class AlipaySecurityRiskGravityConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskGravityConsultResponse, self).__init__()
        self._error_code = None
        self._error_message = None
        self._extension = None
        self._header = None
        self._process_success = None
        self._risk_result = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        if isinstance(value, list):
            self._extension = list()
            for i in value:
                if isinstance(i, GravityParam):
                    self._extension.append(i)
                else:
                    self._extension.append(GravityParam.from_alipay_dict(i))
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, SecGravityServiceHeader):
            self._header = value
        else:
            self._header = SecGravityServiceHeader.from_alipay_dict(value)
    @property
    def process_success(self):
        return self._process_success

    @process_success.setter
    def process_success(self, value):
        self._process_success = value
    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, list):
            self._risk_result = list()
            for i in value:
                if isinstance(i, GravityRiskResult):
                    self._risk_result.append(i)
                else:
                    self._risk_result.append(GravityRiskResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskGravityConsultResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'extension' in response:
            self.extension = response['extension']
        if 'header' in response:
            self.header = response['header']
        if 'process_success' in response:
            self.process_success = response['process_success']
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
