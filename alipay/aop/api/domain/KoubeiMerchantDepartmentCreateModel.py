#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantDepartmentCreateModel(object):

    def __init__(self):
        self._auth_code = None
        self._dept_name = None
        self._label_code = None
        self._parent_dept_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def parent_dept_id(self):
        return self._parent_dept_id

    @parent_dept_id.setter
    def parent_dept_id(self, value):
        self._parent_dept_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
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
        o = KoubeiMerchantDepartmentCreateModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'parent_dept_id' in d:
            o.parent_dept_id = d['parent_dept_id']
        return o


