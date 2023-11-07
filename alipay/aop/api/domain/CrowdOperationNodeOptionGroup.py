#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdOperationNodeOption import CrowdOperationNodeOption


class CrowdOperationNodeOptionGroup(object):

    def __init__(self):
        self._code = None
        self._node_option_list = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def node_option_list(self):
        return self._node_option_list

    @node_option_list.setter
    def node_option_list(self, value):
        if isinstance(value, list):
            self._node_option_list = list()
            for i in value:
                if isinstance(i, CrowdOperationNodeOption):
                    self._node_option_list.append(i)
                else:
                    self._node_option_list.append(CrowdOperationNodeOption.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.node_option_list:
            if isinstance(self.node_option_list, list):
                for i in range(0, len(self.node_option_list)):
                    element = self.node_option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_option_list[i] = element.to_alipay_dict()
            if hasattr(self.node_option_list, 'to_alipay_dict'):
                params['node_option_list'] = self.node_option_list.to_alipay_dict()
            else:
                params['node_option_list'] = self.node_option_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdOperationNodeOptionGroup()
        if 'code' in d:
            o.code = d['code']
        if 'node_option_list' in d:
            o.node_option_list = d['node_option_list']
        return o


