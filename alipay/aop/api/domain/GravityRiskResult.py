#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GravityRiskResult(object):

    def __init__(self):
        self._risk_rank = None
        self._risk_tag = None

    @property
    def risk_rank(self):
        return self._risk_rank

    @risk_rank.setter
    def risk_rank(self, value):
        self._risk_rank = value
    @property
    def risk_tag(self):
        return self._risk_tag

    @risk_tag.setter
    def risk_tag(self, value):
        self._risk_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_rank:
            if hasattr(self.risk_rank, 'to_alipay_dict'):
                params['risk_rank'] = self.risk_rank.to_alipay_dict()
            else:
                params['risk_rank'] = self.risk_rank
        if self.risk_tag:
            if hasattr(self.risk_tag, 'to_alipay_dict'):
                params['risk_tag'] = self.risk_tag.to_alipay_dict()
            else:
                params['risk_tag'] = self.risk_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GravityRiskResult()
        if 'risk_rank' in d:
            o.risk_rank = d['risk_rank']
        if 'risk_tag' in d:
            o.risk_tag = d['risk_tag']
        return o


