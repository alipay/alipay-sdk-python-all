#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskEvaluationResult import RiskEvaluationResult


class AlipayDigitalmgmtAnticgovernanceRiskevaluationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtAnticgovernanceRiskevaluationQueryResponse, self).__init__()
        self._risk_evaluation_result = None

    @property
    def risk_evaluation_result(self):
        return self._risk_evaluation_result

    @risk_evaluation_result.setter
    def risk_evaluation_result(self, value):
        if isinstance(value, RiskEvaluationResult):
            self._risk_evaluation_result = value
        else:
            self._risk_evaluation_result = RiskEvaluationResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtAnticgovernanceRiskevaluationQueryResponse, self).parse_response_content(response_content)
        if 'risk_evaluation_result' in response:
            self.risk_evaluation_result = response['risk_evaluation_result']
