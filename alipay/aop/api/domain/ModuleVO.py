#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ModuleValueVO import ModuleValueVO


class ModuleVO(object):

    def __init__(self):
        self._module_code = None
        self._module_name = None
        self._module_value_items = None
        self._rule_conditions = None

    @property
    def module_code(self):
        return self._module_code

    @module_code.setter
    def module_code(self, value):
        self._module_code = value
    @property
    def module_name(self):
        return self._module_name

    @module_name.setter
    def module_name(self, value):
        self._module_name = value
    @property
    def module_value_items(self):
        return self._module_value_items

    @module_value_items.setter
    def module_value_items(self, value):
        if isinstance(value, list):
            self._module_value_items = list()
            for i in value:
                if isinstance(i, ModuleValueVO):
                    self._module_value_items.append(i)
                else:
                    self._module_value_items.append(ModuleValueVO.from_alipay_dict(i))
    @property
    def rule_conditions(self):
        return self._rule_conditions

    @rule_conditions.setter
    def rule_conditions(self, value):
        self._rule_conditions = value


    def to_alipay_dict(self):
        params = dict()
        if self.module_code:
            if hasattr(self.module_code, 'to_alipay_dict'):
                params['module_code'] = self.module_code.to_alipay_dict()
            else:
                params['module_code'] = self.module_code
        if self.module_name:
            if hasattr(self.module_name, 'to_alipay_dict'):
                params['module_name'] = self.module_name.to_alipay_dict()
            else:
                params['module_name'] = self.module_name
        if self.module_value_items:
            if isinstance(self.module_value_items, list):
                for i in range(0, len(self.module_value_items)):
                    element = self.module_value_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.module_value_items[i] = element.to_alipay_dict()
            if hasattr(self.module_value_items, 'to_alipay_dict'):
                params['module_value_items'] = self.module_value_items.to_alipay_dict()
            else:
                params['module_value_items'] = self.module_value_items
        if self.rule_conditions:
            if hasattr(self.rule_conditions, 'to_alipay_dict'):
                params['rule_conditions'] = self.rule_conditions.to_alipay_dict()
            else:
                params['rule_conditions'] = self.rule_conditions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModuleVO()
        if 'module_code' in d:
            o.module_code = d['module_code']
        if 'module_name' in d:
            o.module_name = d['module_name']
        if 'module_value_items' in d:
            o.module_value_items = d['module_value_items']
        if 'rule_conditions' in d:
            o.rule_conditions = d['rule_conditions']
        return o


