#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomerDefineDeductRule import CustomerDefineDeductRule


class DeductInfo(object):

    def __init__(self):
        self._customer_define_deduct_rule = None

    @property
    def customer_define_deduct_rule(self):
        return self._customer_define_deduct_rule

    @customer_define_deduct_rule.setter
    def customer_define_deduct_rule(self, value):
        if isinstance(value, CustomerDefineDeductRule):
            self._customer_define_deduct_rule = value
        else:
            self._customer_define_deduct_rule = CustomerDefineDeductRule.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.customer_define_deduct_rule:
            if hasattr(self.customer_define_deduct_rule, 'to_alipay_dict'):
                params['customer_define_deduct_rule'] = self.customer_define_deduct_rule.to_alipay_dict()
            else:
                params['customer_define_deduct_rule'] = self.customer_define_deduct_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductInfo()
        if 'customer_define_deduct_rule' in d:
            o.customer_define_deduct_rule = d['customer_define_deduct_rule']
        return o


