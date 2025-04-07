#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ControlRuleVO(object):

    def __init__(self):
        self._rule_key = None
        self._rule_value = None

    @property
    def rule_key(self):
        return self._rule_key

    @rule_key.setter
    def rule_key(self, value):
        self._rule_key = value
    @property
    def rule_value(self):
        return self._rule_value

    @rule_value.setter
    def rule_value(self, value):
        self._rule_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_key:
            if hasattr(self.rule_key, 'to_alipay_dict'):
                params['rule_key'] = self.rule_key.to_alipay_dict()
            else:
                params['rule_key'] = self.rule_key
        if self.rule_value:
            if hasattr(self.rule_value, 'to_alipay_dict'):
                params['rule_value'] = self.rule_value.to_alipay_dict()
            else:
                params['rule_value'] = self.rule_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ControlRuleVO()
        if 'rule_key' in d:
            o.rule_key = d['rule_key']
        if 'rule_value' in d:
            o.rule_value = d['rule_value']
        return o


