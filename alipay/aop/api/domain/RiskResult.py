#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskResult(object):

    def __init__(self):
        self._risk_type = None
        self._score = None

    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskResult()
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'score' in d:
            o.score = d['score']
        return o


