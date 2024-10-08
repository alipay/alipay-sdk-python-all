#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleDefine import RuleDefine


class WalletUseRule(object):

    def __init__(self):
        self._merchant_rule = None
        self._rule_define = None

    @property
    def merchant_rule(self):
        return self._merchant_rule

    @merchant_rule.setter
    def merchant_rule(self, value):
        self._merchant_rule = value
    @property
    def rule_define(self):
        return self._rule_define

    @rule_define.setter
    def rule_define(self, value):
        if isinstance(value, RuleDefine):
            self._rule_define = value
        else:
            self._rule_define = RuleDefine.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_rule:
            if hasattr(self.merchant_rule, 'to_alipay_dict'):
                params['merchant_rule'] = self.merchant_rule.to_alipay_dict()
            else:
                params['merchant_rule'] = self.merchant_rule
        if self.rule_define:
            if hasattr(self.rule_define, 'to_alipay_dict'):
                params['rule_define'] = self.rule_define.to_alipay_dict()
            else:
                params['rule_define'] = self.rule_define
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletUseRule()
        if 'merchant_rule' in d:
            o.merchant_rule = d['merchant_rule']
        if 'rule_define' in d:
            o.rule_define = d['rule_define']
        return o


