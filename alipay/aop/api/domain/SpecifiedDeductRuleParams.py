#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifiedDeductRuleParams(object):

    def __init__(self):
        self._specified_pay_amount = None
        self._specified_pay_trigger_amount = None
        self._specified_pay_trigger_unit = None

    @property
    def specified_pay_amount(self):
        return self._specified_pay_amount

    @specified_pay_amount.setter
    def specified_pay_amount(self, value):
        self._specified_pay_amount = value
    @property
    def specified_pay_trigger_amount(self):
        return self._specified_pay_trigger_amount

    @specified_pay_trigger_amount.setter
    def specified_pay_trigger_amount(self, value):
        self._specified_pay_trigger_amount = value
    @property
    def specified_pay_trigger_unit(self):
        return self._specified_pay_trigger_unit

    @specified_pay_trigger_unit.setter
    def specified_pay_trigger_unit(self, value):
        self._specified_pay_trigger_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.specified_pay_amount:
            if hasattr(self.specified_pay_amount, 'to_alipay_dict'):
                params['specified_pay_amount'] = self.specified_pay_amount.to_alipay_dict()
            else:
                params['specified_pay_amount'] = self.specified_pay_amount
        if self.specified_pay_trigger_amount:
            if hasattr(self.specified_pay_trigger_amount, 'to_alipay_dict'):
                params['specified_pay_trigger_amount'] = self.specified_pay_trigger_amount.to_alipay_dict()
            else:
                params['specified_pay_trigger_amount'] = self.specified_pay_trigger_amount
        if self.specified_pay_trigger_unit:
            if hasattr(self.specified_pay_trigger_unit, 'to_alipay_dict'):
                params['specified_pay_trigger_unit'] = self.specified_pay_trigger_unit.to_alipay_dict()
            else:
                params['specified_pay_trigger_unit'] = self.specified_pay_trigger_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifiedDeductRuleParams()
        if 'specified_pay_amount' in d:
            o.specified_pay_amount = d['specified_pay_amount']
        if 'specified_pay_trigger_amount' in d:
            o.specified_pay_trigger_amount = d['specified_pay_trigger_amount']
        if 'specified_pay_trigger_unit' in d:
            o.specified_pay_trigger_unit = d['specified_pay_trigger_unit']
        return o


