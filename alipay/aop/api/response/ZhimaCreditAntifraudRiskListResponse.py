#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditAntifraudRiskListResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditAntifraudRiskListResponse, self).__init__()
        self._biz_no = None
        self._decision_result = None
        self._hit_risk = None
        self._risk_code = None
        self._solution_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def decision_result(self):
        return self._decision_result

    @decision_result.setter
    def decision_result(self, value):
        self._decision_result = value
    @property
    def hit_risk(self):
        return self._hit_risk

    @hit_risk.setter
    def hit_risk(self, value):
        self._hit_risk = value
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
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditAntifraudRiskListResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'decision_result' in response:
            self.decision_result = response['decision_result']
        if 'hit_risk' in response:
            self.hit_risk = response['hit_risk']
        if 'risk_code' in response:
            self.risk_code = response['risk_code']
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
