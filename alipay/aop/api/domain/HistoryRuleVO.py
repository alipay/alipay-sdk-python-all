#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HistoryRuleVO(object):

    def __init__(self):
        self._last_modified_time = None
        self._module_code = None
        self._outer_product_code = None
        self._rule_conditions = None
        self._rule_id = None

    @property
    def last_modified_time(self):
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, value):
        self._last_modified_time = value
    @property
    def module_code(self):
        return self._module_code

    @module_code.setter
    def module_code(self, value):
        self._module_code = value
    @property
    def outer_product_code(self):
        return self._outer_product_code

    @outer_product_code.setter
    def outer_product_code(self, value):
        self._outer_product_code = value
    @property
    def rule_conditions(self):
        return self._rule_conditions

    @rule_conditions.setter
    def rule_conditions(self, value):
        self._rule_conditions = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_modified_time:
            if hasattr(self.last_modified_time, 'to_alipay_dict'):
                params['last_modified_time'] = self.last_modified_time.to_alipay_dict()
            else:
                params['last_modified_time'] = self.last_modified_time
        if self.module_code:
            if hasattr(self.module_code, 'to_alipay_dict'):
                params['module_code'] = self.module_code.to_alipay_dict()
            else:
                params['module_code'] = self.module_code
        if self.outer_product_code:
            if hasattr(self.outer_product_code, 'to_alipay_dict'):
                params['outer_product_code'] = self.outer_product_code.to_alipay_dict()
            else:
                params['outer_product_code'] = self.outer_product_code
        if self.rule_conditions:
            if hasattr(self.rule_conditions, 'to_alipay_dict'):
                params['rule_conditions'] = self.rule_conditions.to_alipay_dict()
            else:
                params['rule_conditions'] = self.rule_conditions
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HistoryRuleVO()
        if 'last_modified_time' in d:
            o.last_modified_time = d['last_modified_time']
        if 'module_code' in d:
            o.module_code = d['module_code']
        if 'outer_product_code' in d:
            o.outer_product_code = d['outer_product_code']
        if 'rule_conditions' in d:
            o.rule_conditions = d['rule_conditions']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        return o


