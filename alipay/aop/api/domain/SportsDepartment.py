#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SportsDepartment(object):

    def __init__(self):
        self._department_code = None
        self._leaf = None
        self._level = None
        self._name = None
        self._parent_code = None

    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def leaf(self):
        return self._leaf

    @leaf.setter
    def leaf(self, value):
        self._leaf = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.leaf:
            if hasattr(self.leaf, 'to_alipay_dict'):
                params['leaf'] = self.leaf.to_alipay_dict()
            else:
                params['leaf'] = self.leaf
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SportsDepartment()
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'leaf' in d:
            o.leaf = d['leaf']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        return o


