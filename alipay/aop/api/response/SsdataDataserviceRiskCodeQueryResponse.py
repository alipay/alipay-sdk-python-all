#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskCodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskCodeQueryResponse, self).__init__()
        self._hit = None
        self._risk_code = None
        self._unique_id = None
        self._verify_code = None

    @property
    def hit(self):
        return self._hit

    @hit.setter
    def hit(self, value):
        self._hit = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        if isinstance(value, list):
            self._risk_code = list()
            for i in value:
                self._risk_code.append(i)
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        if isinstance(value, list):
            self._verify_code = list()
            for i in value:
                self._verify_code.append(i)

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskCodeQueryResponse, self).parse_response_content(response_content)
        if 'hit' in response:
            self.hit = response['hit']
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
        if 'verify_code' in response:
            self.verify_code = response['verify_code']
