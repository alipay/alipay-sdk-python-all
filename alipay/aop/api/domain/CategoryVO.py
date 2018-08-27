#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryVO(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._description = None
        self._enable = None
        self._level = None
        self._parent_id = None
        self._root_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def root_id(self):
        return self._root_id

    @root_id.setter
    def root_id(self, value):
        self._root_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.root_id:
            if hasattr(self.root_id, 'to_alipay_dict'):
                params['root_id'] = self.root_id.to_alipay_dict()
            else:
                params['root_id'] = self.root_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'description' in d:
            o.description = d['description']
        if 'enable' in d:
            o.enable = d['enable']
        if 'level' in d:
            o.level = d['level']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'root_id' in d:
            o.root_id = d['root_id']
        return o


