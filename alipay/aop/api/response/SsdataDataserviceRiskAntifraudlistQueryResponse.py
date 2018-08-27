#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAntifraudlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAntifraudlistQueryResponse, self).__init__()
        self._biz_no = None
        self._hit = None
        self._risk_code = None
        self._unique_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
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
        self._risk_code = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAntifraudlistQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'hit' in response:
            self.hit = response['hit']
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
