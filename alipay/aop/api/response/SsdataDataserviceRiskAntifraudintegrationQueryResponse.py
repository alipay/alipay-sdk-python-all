#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskAntifraudintegrationQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskAntifraudintegrationQueryResponse, self).__init__()
        self._biz_no = None
        self._hit = None
        self._risk_code = None
        self._score = None
        self._unique_id = None
        self._verify_code = None

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
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
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
        self._verify_code = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskAntifraudintegrationQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'hit' in response:
            self.hit = response['hit']
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'score' in response:
            self.score = response['score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
        if 'verify_code' in response:
            self.verify_code = response['verify_code']
