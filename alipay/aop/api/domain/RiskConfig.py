#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CategoryRiskInfo import CategoryRiskInfo
from alipay.aop.api.domain.QuotaGradientRule import QuotaGradientRule


class RiskConfig(object):

    def __init__(self):
        self._category_risks = None
        self._quota_gradient_rule = None

    @property
    def category_risks(self):
        return self._category_risks

    @category_risks.setter
    def category_risks(self, value):
        if isinstance(value, list):
            self._category_risks = list()
            for i in value:
                if isinstance(i, CategoryRiskInfo):
                    self._category_risks.append(i)
                else:
                    self._category_risks.append(CategoryRiskInfo.from_alipay_dict(i))
    @property
    def quota_gradient_rule(self):
        return self._quota_gradient_rule

    @quota_gradient_rule.setter
    def quota_gradient_rule(self, value):
        if isinstance(value, QuotaGradientRule):
            self._quota_gradient_rule = value
        else:
            self._quota_gradient_rule = QuotaGradientRule.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.category_risks:
            if isinstance(self.category_risks, list):
                for i in range(0, len(self.category_risks)):
                    element = self.category_risks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_risks[i] = element.to_alipay_dict()
            if hasattr(self.category_risks, 'to_alipay_dict'):
                params['category_risks'] = self.category_risks.to_alipay_dict()
            else:
                params['category_risks'] = self.category_risks
        if self.quota_gradient_rule:
            if hasattr(self.quota_gradient_rule, 'to_alipay_dict'):
                params['quota_gradient_rule'] = self.quota_gradient_rule.to_alipay_dict()
            else:
                params['quota_gradient_rule'] = self.quota_gradient_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskConfig()
        if 'category_risks' in d:
            o.category_risks = d['category_risks']
        if 'quota_gradient_rule' in d:
            o.quota_gradient_rule = d['quota_gradient_rule']
        return o


