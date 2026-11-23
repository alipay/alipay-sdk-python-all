#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZhimaRiskDetail import ZhimaRiskDetail


class AliTrustRiskIdentify(object):

    def __init__(self):
        self._details = None
        self._is_risk = None
        self._risk_tag = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, ZhimaRiskDetail):
                    self._details.append(i)
                else:
                    self._details.append(ZhimaRiskDetail.from_alipay_dict(i))
    @property
    def is_risk(self):
        return self._is_risk

    @is_risk.setter
    def is_risk(self, value):
        self._is_risk = value
    @property
    def risk_tag(self):
        return self._risk_tag

    @risk_tag.setter
    def risk_tag(self, value):
        self._risk_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.is_risk:
            if hasattr(self.is_risk, 'to_alipay_dict'):
                params['is_risk'] = self.is_risk.to_alipay_dict()
            else:
                params['is_risk'] = self.is_risk
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
        o = AliTrustRiskIdentify()
        if 'details' in d:
            o.details = d['details']
        if 'is_risk' in d:
            o.is_risk = d['is_risk']
        if 'risk_tag' in d:
            o.risk_tag = d['risk_tag']
        return o


