#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskpluscoreRiskQueryResult import RiskpluscoreRiskQueryResult


class AlipaySecurityRiskMiniprogramNsfQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskMiniprogramNsfQueryResponse, self).__init__()
        self._risk_result = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, RiskpluscoreRiskQueryResult):
            self._risk_result = value
        else:
            self._risk_result = RiskpluscoreRiskQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskMiniprogramNsfQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
