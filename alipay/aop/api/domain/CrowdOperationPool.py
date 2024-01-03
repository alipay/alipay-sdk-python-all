#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdOperationNode import CrowdOperationNode


class CrowdOperationPool(object):

    def __init__(self):
        self._crowd_pool_code = None
        self._crowd_pool_type = None
        self._in_operation_type = None
        self._node_list = None
        self._out_operation_type = None

    @property
    def crowd_pool_code(self):
        return self._crowd_pool_code

    @crowd_pool_code.setter
    def crowd_pool_code(self, value):
        self._crowd_pool_code = value
    @property
    def crowd_pool_type(self):
        return self._crowd_pool_type

    @crowd_pool_type.setter
    def crowd_pool_type(self, value):
        self._crowd_pool_type = value
    @property
    def in_operation_type(self):
        return self._in_operation_type

    @in_operation_type.setter
    def in_operation_type(self, value):
        self._in_operation_type = value
    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, CrowdOperationNode):
                    self._node_list.append(i)
                else:
                    self._node_list.append(CrowdOperationNode.from_alipay_dict(i))
    @property
    def out_operation_type(self):
        return self._out_operation_type

    @out_operation_type.setter
    def out_operation_type(self, value):
        self._out_operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_pool_code:
            if hasattr(self.crowd_pool_code, 'to_alipay_dict'):
                params['crowd_pool_code'] = self.crowd_pool_code.to_alipay_dict()
            else:
                params['crowd_pool_code'] = self.crowd_pool_code
        if self.crowd_pool_type:
            if hasattr(self.crowd_pool_type, 'to_alipay_dict'):
                params['crowd_pool_type'] = self.crowd_pool_type.to_alipay_dict()
            else:
                params['crowd_pool_type'] = self.crowd_pool_type
        if self.in_operation_type:
            if hasattr(self.in_operation_type, 'to_alipay_dict'):
                params['in_operation_type'] = self.in_operation_type.to_alipay_dict()
            else:
                params['in_operation_type'] = self.in_operation_type
        if self.node_list:
            if isinstance(self.node_list, list):
                for i in range(0, len(self.node_list)):
                    element = self.node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_list[i] = element.to_alipay_dict()
            if hasattr(self.node_list, 'to_alipay_dict'):
                params['node_list'] = self.node_list.to_alipay_dict()
            else:
                params['node_list'] = self.node_list
        if self.out_operation_type:
            if hasattr(self.out_operation_type, 'to_alipay_dict'):
                params['out_operation_type'] = self.out_operation_type.to_alipay_dict()
            else:
                params['out_operation_type'] = self.out_operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdOperationPool()
        if 'crowd_pool_code' in d:
            o.crowd_pool_code = d['crowd_pool_code']
        if 'crowd_pool_type' in d:
            o.crowd_pool_type = d['crowd_pool_type']
        if 'in_operation_type' in d:
            o.in_operation_type = d['in_operation_type']
        if 'node_list' in d:
            o.node_list = d['node_list']
        if 'out_operation_type' in d:
            o.out_operation_type = d['out_operation_type']
        return o


