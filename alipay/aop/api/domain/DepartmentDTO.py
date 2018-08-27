#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepartmentDTO(object):

    def __init__(self):
        self._biz_type = None
        self._dept_id = None
        self._dept_name = None
        self._dept_path = None
        self._label_code = None
        self._label_name = None
        self._parent_dept_id = None
        self._shop_id = None
        self._type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def dept_path(self):
        return self._dept_path

    @dept_path.setter
    def dept_path(self, value):
        self._dept_path = value
    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def parent_dept_id(self):
        return self._parent_dept_id

    @parent_dept_id.setter
    def parent_dept_id(self, value):
        self._parent_dept_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.dept_path:
            if hasattr(self.dept_path, 'to_alipay_dict'):
                params['dept_path'] = self.dept_path.to_alipay_dict()
            else:
                params['dept_path'] = self.dept_path
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.parent_dept_id:
            if hasattr(self.parent_dept_id, 'to_alipay_dict'):
                params['parent_dept_id'] = self.parent_dept_id.to_alipay_dict()
            else:
                params['parent_dept_id'] = self.parent_dept_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepartmentDTO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'dept_path' in d:
            o.dept_path = d['dept_path']
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'parent_dept_id' in d:
            o.parent_dept_id = d['parent_dept_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'type' in d:
            o.type = d['type']
        return o


