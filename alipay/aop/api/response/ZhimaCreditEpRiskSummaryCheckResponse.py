#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpRiskSummaryCheckResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRiskSummaryCheckResponse, self).__init__()
        self._has_risk = None

    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRiskSummaryCheckResponse, self).parse_response_content(response_content)
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
