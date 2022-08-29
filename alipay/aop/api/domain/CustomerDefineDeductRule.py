#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerDefineDeductRule(object):

    def __init__(self):
        self._customer_define_deduct_rule_desc = None

    @property
    def customer_define_deduct_rule_desc(self):
        return self._customer_define_deduct_rule_desc

    @customer_define_deduct_rule_desc.setter
    def customer_define_deduct_rule_desc(self, value):
        self._customer_define_deduct_rule_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_define_deduct_rule_desc:
            if hasattr(self.customer_define_deduct_rule_desc, 'to_alipay_dict'):
                params['customer_define_deduct_rule_desc'] = self.customer_define_deduct_rule_desc.to_alipay_dict()
            else:
                params['customer_define_deduct_rule_desc'] = self.customer_define_deduct_rule_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerDefineDeductRule()
        if 'customer_define_deduct_rule_desc' in d:
            o.customer_define_deduct_rule_desc = d['customer_define_deduct_rule_desc']
        return o


