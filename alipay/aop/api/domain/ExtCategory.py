#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtCategory(object):

    def __init__(self):
        self._category_code = None
        self._name = None
        self._parent_id = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtCategory()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'name' in d:
            o.name = d['name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        return o


