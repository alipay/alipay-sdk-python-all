#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskEvaluationQueryRequest import RiskEvaluationQueryRequest


class AlipayDigitalmgmtAnticgovernanceRiskevaluationQueryModel(object):

    def __init__(self):
        self._risk_evaluation_query_request = None

    @property
    def risk_evaluation_query_request(self):
        return self._risk_evaluation_query_request

    @risk_evaluation_query_request.setter
    def risk_evaluation_query_request(self, value):
        if isinstance(value, RiskEvaluationQueryRequest):
            self._risk_evaluation_query_request = value
        else:
            self._risk_evaluation_query_request = RiskEvaluationQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.risk_evaluation_query_request:
            if hasattr(self.risk_evaluation_query_request, 'to_alipay_dict'):
                params['risk_evaluation_query_request'] = self.risk_evaluation_query_request.to_alipay_dict()
            else:
                params['risk_evaluation_query_request'] = self.risk_evaluation_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtAnticgovernanceRiskevaluationQueryModel()
        if 'risk_evaluation_query_request' in d:
            o.risk_evaluation_query_request = d['risk_evaluation_query_request']
        return o


