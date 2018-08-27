#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryLevelInfo(object):

    def __init__(self):
        self._category_code = None
        self._category_level = None
        self._category_name = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_level(self):
        return self._category_level

    @category_level.setter
    def category_level(self, value):
        self._category_level = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_level:
            if hasattr(self.category_level, 'to_alipay_dict'):
                params['category_level'] = self.category_level.to_alipay_dict()
            else:
                params['category_level'] = self.category_level
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryLevelInfo()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_level' in d:
            o.category_level = d['category_level']
        if 'category_name' in d:
            o.category_name = d['category_name']
        return o


