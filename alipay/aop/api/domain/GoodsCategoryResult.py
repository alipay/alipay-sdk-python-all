#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsCategoryResult(object):

    def __init__(self):
        self._category_code = None
        self._category_name = None
        self._level = None
        self._parent_category_code = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def parent_category_code(self):
        return self._parent_category_code

    @parent_category_code.setter
    def parent_category_code(self, value):
        self._parent_category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.parent_category_code:
            if hasattr(self.parent_category_code, 'to_alipay_dict'):
                params['parent_category_code'] = self.parent_category_code.to_alipay_dict()
            else:
                params['parent_category_code'] = self.parent_category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsCategoryResult()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'level' in d:
            o.level = d['level']
        if 'parent_category_code' in d:
            o.parent_category_code = d['parent_category_code']
        return o


