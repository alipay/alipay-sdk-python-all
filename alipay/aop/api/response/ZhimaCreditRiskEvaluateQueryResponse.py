#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditRiskEvaluateQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditRiskEvaluateQueryResponse, self).__init__()
        self._accessible = None
        self._biz_no = None
        self._limit_level = None
        self._risk_code = None
        self._score_level = None

    @property
    def accessible(self):
        return self._accessible

    @accessible.setter
    def accessible(self, value):
        self._accessible = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def limit_level(self):
        return self._limit_level

    @limit_level.setter
    def limit_level(self, value):
        self._limit_level = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def score_level(self):
        return self._score_level

    @score_level.setter
    def score_level(self, value):
        self._score_level = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditRiskEvaluateQueryResponse, self).parse_response_content(response_content)
        if 'accessible' in response:
            self.accessible = response['accessible']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'limit_level' in response:
            self.limit_level = response['limit_level']
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'score_level' in response:
            self.score_level = response['score_level']
