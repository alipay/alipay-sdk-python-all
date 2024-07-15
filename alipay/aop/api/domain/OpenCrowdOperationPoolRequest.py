#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenCrowdOperationNodeRequest import OpenCrowdOperationNodeRequest


class OpenCrowdOperationPoolRequest(object):

    def __init__(self):
        self._crowd_pool_type = None
        self._in_operation_type = None
        self._operation_node_list = None
        self._out_operation_type = None

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
    def operation_node_list(self):
        return self._operation_node_list

    @operation_node_list.setter
    def operation_node_list(self, value):
        if isinstance(value, list):
            self._operation_node_list = list()
            for i in value:
                if isinstance(i, OpenCrowdOperationNodeRequest):
                    self._operation_node_list.append(i)
                else:
                    self._operation_node_list.append(OpenCrowdOperationNodeRequest.from_alipay_dict(i))
    @property
    def out_operation_type(self):
        return self._out_operation_type

    @out_operation_type.setter
    def out_operation_type(self, value):
        self._out_operation_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.operation_node_list:
            if isinstance(self.operation_node_list, list):
                for i in range(0, len(self.operation_node_list)):
                    element = self.operation_node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_node_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_node_list, 'to_alipay_dict'):
                params['operation_node_list'] = self.operation_node_list.to_alipay_dict()
            else:
                params['operation_node_list'] = self.operation_node_list
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
        o = OpenCrowdOperationPoolRequest()
        if 'crowd_pool_type' in d:
            o.crowd_pool_type = d['crowd_pool_type']
        if 'in_operation_type' in d:
            o.in_operation_type = d['in_operation_type']
        if 'operation_node_list' in d:
            o.operation_node_list = d['operation_node_list']
        if 'out_operation_type' in d:
            o.out_operation_type = d['out_operation_type']
        return o


