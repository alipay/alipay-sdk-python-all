#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitUseLimitDTO import BenefitUseLimitDTO
from alipay.aop.api.domain.BenefitValidPeriodDTO import BenefitValidPeriodDTO
from alipay.aop.api.domain.BenefitUsageScopeDTO import BenefitUsageScopeDTO


class BenefitUseRuleDTO(object):

    def __init__(self):
        self._benefit_use_limit = None
        self._benefit_valid_period = None
        self._usage_scope = None

    @property
    def benefit_use_limit(self):
        return self._benefit_use_limit

    @benefit_use_limit.setter
    def benefit_use_limit(self, value):
        if isinstance(value, BenefitUseLimitDTO):
            self._benefit_use_limit = value
        else:
            self._benefit_use_limit = BenefitUseLimitDTO.from_alipay_dict(value)
    @property
    def benefit_valid_period(self):
        return self._benefit_valid_period

    @benefit_valid_period.setter
    def benefit_valid_period(self, value):
        if isinstance(value, BenefitValidPeriodDTO):
            self._benefit_valid_period = value
        else:
            self._benefit_valid_period = BenefitValidPeriodDTO.from_alipay_dict(value)
    @property
    def usage_scope(self):
        return self._usage_scope

    @usage_scope.setter
    def usage_scope(self, value):
        if isinstance(value, BenefitUsageScopeDTO):
            self._usage_scope = value
        else:
            self._usage_scope = BenefitUsageScopeDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_use_limit:
            if hasattr(self.benefit_use_limit, 'to_alipay_dict'):
                params['benefit_use_limit'] = self.benefit_use_limit.to_alipay_dict()
            else:
                params['benefit_use_limit'] = self.benefit_use_limit
        if self.benefit_valid_period:
            if hasattr(self.benefit_valid_period, 'to_alipay_dict'):
                params['benefit_valid_period'] = self.benefit_valid_period.to_alipay_dict()
            else:
                params['benefit_valid_period'] = self.benefit_valid_period
        if self.usage_scope:
            if hasattr(self.usage_scope, 'to_alipay_dict'):
                params['usage_scope'] = self.usage_scope.to_alipay_dict()
            else:
                params['usage_scope'] = self.usage_scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitUseRuleDTO()
        if 'benefit_use_limit' in d:
            o.benefit_use_limit = d['benefit_use_limit']
        if 'benefit_valid_period' in d:
            o.benefit_valid_period = d['benefit_valid_period']
        if 'usage_scope' in d:
            o.usage_scope = d['usage_scope']
        return o


