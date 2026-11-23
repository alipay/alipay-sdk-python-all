#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SocialRiskDetail import SocialRiskDetail


class SocialRiskInfo(object):

    def __init__(self):
        self._has_cases = None
        self._risk_desc = None
        self._risk_detail = None

    @property
    def has_cases(self):
        return self._has_cases

    @has_cases.setter
    def has_cases(self, value):
        self._has_cases = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_detail(self):
        return self._risk_detail

    @risk_detail.setter
    def risk_detail(self, value):
        if isinstance(value, SocialRiskDetail):
            self._risk_detail = value
        else:
            self._risk_detail = SocialRiskDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.has_cases:
            if hasattr(self.has_cases, 'to_alipay_dict'):
                params['has_cases'] = self.has_cases.to_alipay_dict()
            else:
                params['has_cases'] = self.has_cases
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risk_detail:
            if hasattr(self.risk_detail, 'to_alipay_dict'):
                params['risk_detail'] = self.risk_detail.to_alipay_dict()
            else:
                params['risk_detail'] = self.risk_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SocialRiskInfo()
        if 'has_cases' in d:
            o.has_cases = d['has_cases']
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_detail' in d:
            o.risk_detail = d['risk_detail']
        return o


