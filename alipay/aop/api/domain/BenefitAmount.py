#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitAmount(object):

    def __init__(self):
        self._benefit_desc = None
        self._benefit_money = None
        self._type = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        self._benefit_desc = value
    @property
    def benefit_money(self):
        return self._benefit_money

    @benefit_money.setter
    def benefit_money(self, value):
        self._benefit_money = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.benefit_money:
            if hasattr(self.benefit_money, 'to_alipay_dict'):
                params['benefit_money'] = self.benefit_money.to_alipay_dict()
            else:
                params['benefit_money'] = self.benefit_money
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
        o = BenefitAmount()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'benefit_money' in d:
            o.benefit_money = d['benefit_money']
        if 'type' in d:
            o.type = d['type']
        return o


