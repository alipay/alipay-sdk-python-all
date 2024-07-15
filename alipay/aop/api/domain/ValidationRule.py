#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ValidationRule(object):

    def __init__(self):
        self._cons_type = None
        self._error_msg = None
        self._min_amount = None
        self._rule_text = None
        self._rule_type = None

    @property
    def cons_type(self):
        return self._cons_type

    @cons_type.setter
    def cons_type(self, value):
        self._cons_type = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def rule_text(self):
        return self._rule_text

    @rule_text.setter
    def rule_text(self, value):
        self._rule_text = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cons_type:
            if hasattr(self.cons_type, 'to_alipay_dict'):
                params['cons_type'] = self.cons_type.to_alipay_dict()
            else:
                params['cons_type'] = self.cons_type
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.rule_text:
            if hasattr(self.rule_text, 'to_alipay_dict'):
                params['rule_text'] = self.rule_text.to_alipay_dict()
            else:
                params['rule_text'] = self.rule_text
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ValidationRule()
        if 'cons_type' in d:
            o.cons_type = d['cons_type']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'rule_text' in d:
            o.rule_text = d['rule_text']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        return o


