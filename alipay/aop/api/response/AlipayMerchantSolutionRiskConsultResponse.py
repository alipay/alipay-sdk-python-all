#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskWarningInfo import RiskWarningInfo


class AlipayMerchantSolutionRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolutionRiskConsultResponse, self).__init__()
        self._risk_warning_info = None
        self._solution_code = None

    @property
    def risk_warning_info(self):
        return self._risk_warning_info

    @risk_warning_info.setter
    def risk_warning_info(self, value):
        if isinstance(value, list):
            self._risk_warning_info = list()
            for i in value:
                if isinstance(i, RiskWarningInfo):
                    self._risk_warning_info.append(i)
                else:
                    self._risk_warning_info.append(RiskWarningInfo.from_alipay_dict(i))
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolutionRiskConsultResponse, self).parse_response_content(response_content)
        if 'risk_warning_info' in response:
            self.risk_warning_info = response['risk_warning_info']
        if 'solution_code' in response:
            self.solution_code = response['solution_code']
