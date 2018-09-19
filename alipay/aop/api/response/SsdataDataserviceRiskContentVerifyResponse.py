#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskResult import RiskResult


class SsdataDataserviceRiskContentVerifyResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskContentVerifyResponse, self).__init__()
        self._risk_result = None
        self._score = None
        self._unique_id = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, list):
            self._risk_result = list()
            for i in value:
                if isinstance(i, RiskResult):
                    self._risk_result.append(i)
                else:
                    self._risk_result.append(RiskResult.from_alipay_dict(i))
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

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskContentVerifyResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
        if 'score' in response:
            self.score = response['score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
