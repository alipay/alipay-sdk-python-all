#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ValidationRule(object):

    def __init__(self):
        self._error_msg = None
        self._rule_text = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def rule_text(self):
        return self._rule_text

    @rule_text.setter
    def rule_text(self, value):
        self._rule_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.rule_text:
            if hasattr(self.rule_text, 'to_alipay_dict'):
                params['rule_text'] = self.rule_text.to_alipay_dict()
            else:
                params['rule_text'] = self.rule_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ValidationRule()
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'rule_text' in d:
            o.rule_text = d['rule_text']
        return o


