#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LmCategoryVO(object):

    def __init__(self):
        self._category_id = None
        self._leaf = None
        self._level = None
        self._name = None
        self._parent_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
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
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
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
        o = LmCategoryVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'leaf' in d:
            o.leaf = d['leaf']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        return o


