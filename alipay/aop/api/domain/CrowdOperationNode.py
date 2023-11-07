#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdOperationNodeOptionGroup import CrowdOperationNodeOptionGroup


class CrowdOperationNode(object):

    def __init__(self):
        self._node_code = None
        self._node_desc = None
        self._node_name = None
        self._node_option_group = None
        self._node_option_group_id = None
        self._node_show_type = None
        self._node_type = None
        self._parent_node_code = None

    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def node_desc(self):
        return self._node_desc

    @node_desc.setter
    def node_desc(self, value):
        self._node_desc = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def node_option_group(self):
        return self._node_option_group

    @node_option_group.setter
    def node_option_group(self, value):
        if isinstance(value, CrowdOperationNodeOptionGroup):
            self._node_option_group = value
        else:
            self._node_option_group = CrowdOperationNodeOptionGroup.from_alipay_dict(value)
    @property
    def node_option_group_id(self):
        return self._node_option_group_id

    @node_option_group_id.setter
    def node_option_group_id(self, value):
        self._node_option_group_id = value
    @property
    def node_show_type(self):
        return self._node_show_type

    @node_show_type.setter
    def node_show_type(self, value):
        self._node_show_type = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def parent_node_code(self):
        return self._parent_node_code

    @parent_node_code.setter
    def parent_node_code(self, value):
        self._parent_node_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
        if self.node_desc:
            if hasattr(self.node_desc, 'to_alipay_dict'):
                params['node_desc'] = self.node_desc.to_alipay_dict()
            else:
                params['node_desc'] = self.node_desc
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.node_option_group:
            if hasattr(self.node_option_group, 'to_alipay_dict'):
                params['node_option_group'] = self.node_option_group.to_alipay_dict()
            else:
                params['node_option_group'] = self.node_option_group
        if self.node_option_group_id:
            if hasattr(self.node_option_group_id, 'to_alipay_dict'):
                params['node_option_group_id'] = self.node_option_group_id.to_alipay_dict()
            else:
                params['node_option_group_id'] = self.node_option_group_id
        if self.node_show_type:
            if hasattr(self.node_show_type, 'to_alipay_dict'):
                params['node_show_type'] = self.node_show_type.to_alipay_dict()
            else:
                params['node_show_type'] = self.node_show_type
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.parent_node_code:
            if hasattr(self.parent_node_code, 'to_alipay_dict'):
                params['parent_node_code'] = self.parent_node_code.to_alipay_dict()
            else:
                params['parent_node_code'] = self.parent_node_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdOperationNode()
        if 'node_code' in d:
            o.node_code = d['node_code']
        if 'node_desc' in d:
            o.node_desc = d['node_desc']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'node_option_group' in d:
            o.node_option_group = d['node_option_group']
        if 'node_option_group_id' in d:
            o.node_option_group_id = d['node_option_group_id']
        if 'node_show_type' in d:
            o.node_show_type = d['node_show_type']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'parent_node_code' in d:
            o.parent_node_code = d['parent_node_code']
        return o


