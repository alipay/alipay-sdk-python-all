#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenCrowdOperationOptionRequest import OpenCrowdOperationOptionRequest


class OpenCrowdOperationNodeRequest(object):

    def __init__(self):
        self._node_code = None
        self._node_type = None
        self._operation_option_list = None

    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def operation_option_list(self):
        return self._operation_option_list

    @operation_option_list.setter
    def operation_option_list(self, value):
        if isinstance(value, list):
            self._operation_option_list = list()
            for i in value:
                if isinstance(i, OpenCrowdOperationOptionRequest):
                    self._operation_option_list.append(i)
                else:
                    self._operation_option_list.append(OpenCrowdOperationOptionRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.operation_option_list:
            if isinstance(self.operation_option_list, list):
                for i in range(0, len(self.operation_option_list)):
                    element = self.operation_option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_option_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_option_list, 'to_alipay_dict'):
                params['operation_option_list'] = self.operation_option_list.to_alipay_dict()
            else:
                params['operation_option_list'] = self.operation_option_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCrowdOperationNodeRequest()
        if 'node_code' in d:
            o.node_code = d['node_code']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'operation_option_list' in d:
            o.operation_option_list = d['operation_option_list']
        return o


