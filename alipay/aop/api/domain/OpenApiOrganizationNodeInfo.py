#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiOrganizationNodeInfo(object):

    def __init__(self):
        self._name = None
        self._node_id = None
        self._parent_node_id = None
        self._sort = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def parent_node_id(self):
        return self._parent_node_id

    @parent_node_id.setter
    def parent_node_id(self, value):
        self._parent_node_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.parent_node_id:
            if hasattr(self.parent_node_id, 'to_alipay_dict'):
                params['parent_node_id'] = self.parent_node_id.to_alipay_dict()
            else:
                params['parent_node_id'] = self.parent_node_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOrganizationNodeInfo()
        if 'name' in d:
            o.name = d['name']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'parent_node_id' in d:
            o.parent_node_id = d['parent_node_id']
        if 'sort' in d:
            o.sort = d['sort']
        return o


