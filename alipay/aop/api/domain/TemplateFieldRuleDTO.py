#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateFieldRuleDTO(object):

    def __init__(self):
        self._field_name = None
        self._rule_name = None
        self._rule_value = None

    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_value(self):
        return self._rule_value

    @rule_value.setter
    def rule_value(self, value):
        self._rule_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
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
        o = TemplateFieldRuleDTO()
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_value' in d:
            o.rule_value = d['rule_value']
        return o


