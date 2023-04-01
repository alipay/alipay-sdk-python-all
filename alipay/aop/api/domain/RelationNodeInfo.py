#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RelationNodeInfo(object):

    def __init__(self):
        self._node_name = None
        self._node_no = None
        self._node_type = None
        self._relation_code = None
        self._ultimate_ratio = None

    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def node_no(self):
        return self._node_no

    @node_no.setter
    def node_no(self, value):
        self._node_no = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def relation_code(self):
        return self._relation_code

    @relation_code.setter
    def relation_code(self, value):
        self._relation_code = value
    @property
    def ultimate_ratio(self):
        return self._ultimate_ratio

    @ultimate_ratio.setter
    def ultimate_ratio(self, value):
        self._ultimate_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_name:
            if hasattr(self.node_name, 'to_alipay_dict'):
                params['node_name'] = self.node_name.to_alipay_dict()
            else:
                params['node_name'] = self.node_name
        if self.node_no:
            if hasattr(self.node_no, 'to_alipay_dict'):
                params['node_no'] = self.node_no.to_alipay_dict()
            else:
                params['node_no'] = self.node_no
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.relation_code:
            if hasattr(self.relation_code, 'to_alipay_dict'):
                params['relation_code'] = self.relation_code.to_alipay_dict()
            else:
                params['relation_code'] = self.relation_code
        if self.ultimate_ratio:
            if hasattr(self.ultimate_ratio, 'to_alipay_dict'):
                params['ultimate_ratio'] = self.ultimate_ratio.to_alipay_dict()
            else:
                params['ultimate_ratio'] = self.ultimate_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelationNodeInfo()
        if 'node_name' in d:
            o.node_name = d['node_name']
        if 'node_no' in d:
            o.node_no = d['node_no']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'relation_code' in d:
            o.relation_code = d['relation_code']
        if 'ultimate_ratio' in d:
            o.ultimate_ratio = d['ultimate_ratio']
        return o


