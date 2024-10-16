#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PeriodPayBillingRuleDynamicDTO import PeriodPayBillingRuleDynamicDTO
from alipay.aop.api.domain.PeriodPayBillingRuleFixedDTO import PeriodPayBillingRuleFixedDTO


class PeriodPayBillingRuleDTO(object):

    def __init__(self):
        self._dynamic = None
        self._fixed = None
        self._type = None

    @property
    def dynamic(self):
        return self._dynamic

    @dynamic.setter
    def dynamic(self, value):
        if isinstance(value, PeriodPayBillingRuleDynamicDTO):
            self._dynamic = value
        else:
            self._dynamic = PeriodPayBillingRuleDynamicDTO.from_alipay_dict(value)
    @property
    def fixed(self):
        return self._fixed

    @fixed.setter
    def fixed(self, value):
        if isinstance(value, PeriodPayBillingRuleFixedDTO):
            self._fixed = value
        else:
            self._fixed = PeriodPayBillingRuleFixedDTO.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic:
            if hasattr(self.dynamic, 'to_alipay_dict'):
                params['dynamic'] = self.dynamic.to_alipay_dict()
            else:
                params['dynamic'] = self.dynamic
        if self.fixed:
            if hasattr(self.fixed, 'to_alipay_dict'):
                params['fixed'] = self.fixed.to_alipay_dict()
            else:
                params['fixed'] = self.fixed
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PeriodPayBillingRuleDTO()
        if 'dynamic' in d:
            o.dynamic = d['dynamic']
        if 'fixed' in d:
            o.fixed = d['fixed']
        if 'type' in d:
            o.type = d['type']
        return o


