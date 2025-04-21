#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduNodeInfo(object):

    def __init__(self):
        self._inst_id = None
        self._node_id = None
        self._node_logo = None
        self._node_name = None
        self._parent_id = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def node_logo(self):
        return self._node_logo

    @node_logo.setter
    def node_logo(self, value):
        self._node_logo = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.node_id:
            if hasattr(self.node_id, 'to_alipay_dict'):
                params['node_id'] = self.node_id.to_alipay_dict()
            else:
                params['node_id'] = self.node_id
        if self.node_logo:
            if hasattr(self.node_logo, 'to_alipay_dict'):
                params['node_logo'] = self.node_logo.to_alipay_dict()
            else:
                params['node_logo'] = self.node_logo
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
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
        o = EduNodeInfo()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'node_id' in d:
            o.node_id = d['node_id']
        if 'node_logo' in d:
            o.node_logo = d['node_logo']
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        return o


