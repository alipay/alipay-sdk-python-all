#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskDetectionRequest import RiskDetectionRequest


class AlipayBossFncGfcreditcontrolRiskdetectionserviceQueryModel(object):

    def __init__(self):
        self._risk_detection_request = None

    @property
    def risk_detection_request(self):
        return self._risk_detection_request

    @risk_detection_request.setter
    def risk_detection_request(self, value):
        if isinstance(value, RiskDetectionRequest):
            self._risk_detection_request = value
        else:
            self._risk_detection_request = RiskDetectionRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.risk_detection_request:
            if hasattr(self.risk_detection_request, 'to_alipay_dict'):
                params['risk_detection_request'] = self.risk_detection_request.to_alipay_dict()
            else:
                params['risk_detection_request'] = self.risk_detection_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfcreditcontrolRiskdetectionserviceQueryModel()
        if 'risk_detection_request' in d:
            o.risk_detection_request = d['risk_detection_request']
        return o


