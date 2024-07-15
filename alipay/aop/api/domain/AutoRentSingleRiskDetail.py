#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AutoRentSingleRiskDetail(object):

    def __init__(self):
        self._risk_desc = None
        self._risk_level = None
        self._risk_score = None
        self._source = None

    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_score(self):
        return self._risk_score

    @risk_score.setter
    def risk_score(self, value):
        self._risk_score = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_score:
            if hasattr(self.risk_score, 'to_alipay_dict'):
                params['risk_score'] = self.risk_score.to_alipay_dict()
            else:
                params['risk_score'] = self.risk_score
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AutoRentSingleRiskDetail()
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_score' in d:
            o.risk_score = d['risk_score']
        if 'source' in d:
            o.source = d['source']
        return o


