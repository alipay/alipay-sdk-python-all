#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepartmentVO(object):

    def __init__(self):
        self._can_reg = None
        self._dept_id = None
        self._dept_level = None
        self._dept_name = None
        self._parent_dept_id = None

    @property
    def can_reg(self):
        return self._can_reg

    @can_reg.setter
    def can_reg(self, value):
        self._can_reg = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_level(self):
        return self._dept_level

    @dept_level.setter
    def dept_level(self, value):
        self._dept_level = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def parent_dept_id(self):
        return self._parent_dept_id

    @parent_dept_id.setter
    def parent_dept_id(self, value):
        self._parent_dept_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_reg:
            if hasattr(self.can_reg, 'to_alipay_dict'):
                params['can_reg'] = self.can_reg.to_alipay_dict()
            else:
                params['can_reg'] = self.can_reg
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.dept_level:
            if hasattr(self.dept_level, 'to_alipay_dict'):
                params['dept_level'] = self.dept_level.to_alipay_dict()
            else:
                params['dept_level'] = self.dept_level
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.parent_dept_id:
            if hasattr(self.parent_dept_id, 'to_alipay_dict'):
                params['parent_dept_id'] = self.parent_dept_id.to_alipay_dict()
            else:
                params['parent_dept_id'] = self.parent_dept_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepartmentVO()
        if 'can_reg' in d:
            o.can_reg = d['can_reg']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'dept_level' in d:
            o.dept_level = d['dept_level']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'parent_dept_id' in d:
            o.parent_dept_id = d['parent_dept_id']
        return o


