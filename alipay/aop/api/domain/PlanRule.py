#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlanRule(object):

    def __init__(self):
        self._fixed_value = None
        self._range_end_value = None
        self._range_start_value = None
        self._rule_desc = None
        self._rule_name = None
        self._rule_type = None

    @property
    def fixed_value(self):
        return self._fixed_value

    @fixed_value.setter
    def fixed_value(self, value):
        self._fixed_value = value
    @property
    def range_end_value(self):
        return self._range_end_value

    @range_end_value.setter
    def range_end_value(self, value):
        self._range_end_value = value
    @property
    def range_start_value(self):
        return self._range_start_value

    @range_start_value.setter
    def range_start_value(self, value):
        self._range_start_value = value
    @property
    def rule_desc(self):
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, value):
        self._rule_desc = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fixed_value:
            if hasattr(self.fixed_value, 'to_alipay_dict'):
                params['fixed_value'] = self.fixed_value.to_alipay_dict()
            else:
                params['fixed_value'] = self.fixed_value
        if self.range_end_value:
            if hasattr(self.range_end_value, 'to_alipay_dict'):
                params['range_end_value'] = self.range_end_value.to_alipay_dict()
            else:
                params['range_end_value'] = self.range_end_value
        if self.range_start_value:
            if hasattr(self.range_start_value, 'to_alipay_dict'):
                params['range_start_value'] = self.range_start_value.to_alipay_dict()
            else:
                params['range_start_value'] = self.range_start_value
        if self.rule_desc:
            if hasattr(self.rule_desc, 'to_alipay_dict'):
                params['rule_desc'] = self.rule_desc.to_alipay_dict()
            else:
                params['rule_desc'] = self.rule_desc
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
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
        o = PlanRule()
        if 'fixed_value' in d:
            o.fixed_value = d['fixed_value']
        if 'range_end_value' in d:
            o.range_end_value = d['range_end_value']
        if 'range_start_value' in d:
            o.range_start_value = d['range_start_value']
        if 'rule_desc' in d:
            o.rule_desc = d['rule_desc']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        return o


