#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StandardCategoryInfo(object):

    def __init__(self):
        self._category_id = None
        self._is_leaf = None
        self._name = None
        self._parent_id = None
        self._path = None
        self._root_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def is_leaf(self):
        return self._is_leaf

    @is_leaf.setter
    def is_leaf(self, value):
        self._is_leaf = value
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
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
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
        if self.is_leaf:
            if hasattr(self.is_leaf, 'to_alipay_dict'):
                params['is_leaf'] = self.is_leaf.to_alipay_dict()
            else:
                params['is_leaf'] = self.is_leaf
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
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
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
        o = StandardCategoryInfo()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'is_leaf' in d:
            o.is_leaf = d['is_leaf']
        if 'name' in d:
            o.name = d['name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'path' in d:
            o.path = d['path']
        if 'root_id' in d:
            o.root_id = d['root_id']
        return o


