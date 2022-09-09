#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcDepartmentInfoModifyModel(object):

    def __init__(self):
        self._department_code = None
        self._department_id = None
        self._department_name = None
        self._enterprise_id = None
        self._parent_department_id = None

    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def parent_department_id(self):
        return self._parent_department_id

    @parent_department_id.setter
    def parent_department_id(self, value):
        self._parent_department_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.parent_department_id:
            if hasattr(self.parent_department_id, 'to_alipay_dict'):
                params['parent_department_id'] = self.parent_department_id.to_alipay_dict()
            else:
                params['parent_department_id'] = self.parent_department_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcDepartmentInfoModifyModel()
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'parent_department_id' in d:
            o.parent_department_id = d['parent_department_id']
        return o


