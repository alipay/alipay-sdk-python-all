#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCategoryDto(object):

    def __init__(self):
        self._category_name = None
        self._category_type = None
        self._full_path_name = None
        self._node_id = None
        self._path = None
        self._root_node_id = None

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, value):
        self._category_type = value
    @property
    def full_path_name(self):
        return self._full_path_name

    @full_path_name.setter
    def full_path_name(self, value):
        self._full_path_name = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def root_node_id(self):
        return self._root_node_id

    @root_node_id.setter
    def root_node_id(self, value):
        self._root_node_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_type:
            if hasattr(self.category_type, 'to_alipay_dict'):
                params['category_type'] = self.category_type.to_alipay_dict()
            else:
                params['category_type'] = self.category_type
        if self.full_path_name:
            if hasattr(self.full_path_name, 'to_alipay_dict'):
                params['full_path_name'] = self.full_path_name.to_alipay_dict()
            else:
                params['full_path_name'] = self.full_path_name
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.root_node_id:
            if hasattr(self.root_node_id, 'to_alipay_dict'):
                params['root_node_id'] = self.root_node_id.to_alipay_dict()
            else:
                params['root_node_id'] = self.root_node_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCategoryDto()
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_type' in d:
            o.category_type = d['category_type']
        if 'full_path_name' in d:
            o.full_path_name = d['full_path_name']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'path' in d:
            o.path = d['path']
        if 'root_node_id' in d:
            o.root_node_id = d['root_node_id']
        return o


