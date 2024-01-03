#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanTuringtagQueryModel(object):

    def __init__(self):
        self._node_code_list = None

    @property
    def node_code_list(self):
        return self._node_code_list

    @node_code_list.setter
    def node_code_list(self, value):
        if isinstance(value, list):
            self._node_code_list = list()
            for i in value:
                self._node_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.node_code_list:
            if isinstance(self.node_code_list, list):
                for i in range(0, len(self.node_code_list)):
                    element = self.node_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_code_list[i] = element.to_alipay_dict()
            if hasattr(self.node_code_list, 'to_alipay_dict'):
                params['node_code_list'] = self.node_code_list.to_alipay_dict()
            else:
                params['node_code_list'] = self.node_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanTuringtagQueryModel()
        if 'node_code_list' in d:
            o.node_code_list = d['node_code_list']
        return o


