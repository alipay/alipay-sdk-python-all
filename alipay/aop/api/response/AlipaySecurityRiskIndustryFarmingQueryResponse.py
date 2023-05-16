#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskpluscoreRiskQueryResult import RiskpluscoreRiskQueryResult


class AlipaySecurityRiskIndustryFarmingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskIndustryFarmingQueryResponse, self).__init__()
        self._risk_result = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, list):
            self._risk_result = list()
            for i in value:
                if isinstance(i, RiskpluscoreRiskQueryResult):
                    self._risk_result.append(i)
                else:
                    self._risk_result.append(RiskpluscoreRiskQueryResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskIndustryFarmingQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
