#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantCreditlifeRiskApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantCreditlifeRiskApplyResponse, self).__init__()
        self._open_id = None
        self._zm_grade = None
        self._zm_risk = None
        self._zm_score = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def zm_grade(self):
        return self._zm_grade

    @zm_grade.setter
    def zm_grade(self, value):
        self._zm_grade = value
    @property
    def zm_risk(self):
        return self._zm_risk

    @zm_risk.setter
    def zm_risk(self, value):
        self._zm_risk = value
    @property
    def zm_score(self):
        return self._zm_score

    @zm_score.setter
    def zm_score(self, value):
        self._zm_score = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantCreditlifeRiskApplyResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'zm_grade' in response:
            self.zm_grade = response['zm_grade']
        if 'zm_risk' in response:
            self.zm_risk = response['zm_risk']
        if 'zm_score' in response:
            self.zm_score = response['zm_score']
