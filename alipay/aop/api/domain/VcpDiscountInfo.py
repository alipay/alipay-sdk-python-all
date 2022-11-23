#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpCalcRule import VcpCalcRule


class VcpDiscountInfo(object):

    def __init__(self):
        self._calc_rules = None
        self._calc_type_mode = None
        self._ceiling_amount = None
        self._ceiling_count = None
        self._discount_type = None

    @property
    def calc_rules(self):
        return self._calc_rules

    @calc_rules.setter
    def calc_rules(self, value):
        if isinstance(value, list):
            self._calc_rules = list()
            for i in value:
                if isinstance(i, VcpCalcRule):
                    self._calc_rules.append(i)
                else:
                    self._calc_rules.append(VcpCalcRule.from_alipay_dict(i))
    @property
    def calc_type_mode(self):
        return self._calc_type_mode

    @calc_type_mode.setter
    def calc_type_mode(self, value):
        self._calc_type_mode = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def ceiling_count(self):
        return self._ceiling_count

    @ceiling_count.setter
    def ceiling_count(self, value):
        self._ceiling_count = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.calc_rules:
            if isinstance(self.calc_rules, list):
                for i in range(0, len(self.calc_rules)):
                    element = self.calc_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.calc_rules[i] = element.to_alipay_dict()
            if hasattr(self.calc_rules, 'to_alipay_dict'):
                params['calc_rules'] = self.calc_rules.to_alipay_dict()
            else:
                params['calc_rules'] = self.calc_rules
        if self.calc_type_mode:
            if hasattr(self.calc_type_mode, 'to_alipay_dict'):
                params['calc_type_mode'] = self.calc_type_mode.to_alipay_dict()
            else:
                params['calc_type_mode'] = self.calc_type_mode
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.ceiling_count:
            if hasattr(self.ceiling_count, 'to_alipay_dict'):
                params['ceiling_count'] = self.ceiling_count.to_alipay_dict()
            else:
                params['ceiling_count'] = self.ceiling_count
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpDiscountInfo()
        if 'calc_rules' in d:
            o.calc_rules = d['calc_rules']
        if 'calc_type_mode' in d:
            o.calc_type_mode = d['calc_type_mode']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'ceiling_count' in d:
            o.ceiling_count = d['ceiling_count']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        return o


