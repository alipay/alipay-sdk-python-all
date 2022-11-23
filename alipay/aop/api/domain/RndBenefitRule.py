#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RndBenefitRule(object):

    def __init__(self):
        self._max_benefit = None
        self._min_benefit = None
        self._proportion = None

    @property
    def max_benefit(self):
        return self._max_benefit

    @max_benefit.setter
    def max_benefit(self, value):
        self._max_benefit = value
    @property
    def min_benefit(self):
        return self._min_benefit

    @min_benefit.setter
    def min_benefit(self, value):
        self._min_benefit = value
    @property
    def proportion(self):
        return self._proportion

    @proportion.setter
    def proportion(self, value):
        self._proportion = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_benefit:
            if hasattr(self.max_benefit, 'to_alipay_dict'):
                params['max_benefit'] = self.max_benefit.to_alipay_dict()
            else:
                params['max_benefit'] = self.max_benefit
        if self.min_benefit:
            if hasattr(self.min_benefit, 'to_alipay_dict'):
                params['min_benefit'] = self.min_benefit.to_alipay_dict()
            else:
                params['min_benefit'] = self.min_benefit
        if self.proportion:
            if hasattr(self.proportion, 'to_alipay_dict'):
                params['proportion'] = self.proportion.to_alipay_dict()
            else:
                params['proportion'] = self.proportion
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RndBenefitRule()
        if 'max_benefit' in d:
            o.max_benefit = d['max_benefit']
        if 'min_benefit' in d:
            o.min_benefit = d['min_benefit']
        if 'proportion' in d:
            o.proportion = d['proportion']
        return o


