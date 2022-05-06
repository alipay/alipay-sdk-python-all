#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizTreeNodeWithNoRecursive(object):

    def __init__(self):
        self._has_children = None
        self._node_id = None
        self._node_name = None
        self._parent_node_id = None
        self._sequence = None

    @property
    def has_children(self):
        return self._has_children

    @has_children.setter
    def has_children(self, value):
        self._has_children = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def parent_node_id(self):
        return self._parent_node_id

    @parent_node_id.setter
    def parent_node_id(self, value):
        self._parent_node_id = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_children:
            if hasattr(self.has_children, 'to_alipay_dict'):
                params['has_children'] = self.has_children.to_alipay_dict()
            else:
                params['has_children'] = self.has_children
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.parent_node_id:
            if hasattr(self.parent_node_id, 'to_alipay_dict'):
                params['parent_node_id'] = self.parent_node_id.to_alipay_dict()
            else:
                params['parent_node_id'] = self.parent_node_id
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizTreeNodeWithNoRecursive()
        if 'has_children' in d:
            o.has_children = d['has_children']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'parent_node_id' in d:
            o.parent_node_id = d['parent_node_id']
        if 'sequence' in d:
            o.sequence = d['sequence']
        return o


