#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenCrowdOperationPoolRequest import OpenCrowdOperationPoolRequest


class AlipayMarketingQipanCrowdoperationCreateModel(object):

    def __init__(self):
        self._crowd_name = None
        self._operation_pool_list = None

    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def operation_pool_list(self):
        return self._operation_pool_list

    @operation_pool_list.setter
    def operation_pool_list(self, value):
        if isinstance(value, list):
            self._operation_pool_list = list()
            for i in value:
                if isinstance(i, OpenCrowdOperationPoolRequest):
                    self._operation_pool_list.append(i)
                else:
                    self._operation_pool_list.append(OpenCrowdOperationPoolRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.operation_pool_list:
            if isinstance(self.operation_pool_list, list):
                for i in range(0, len(self.operation_pool_list)):
                    element = self.operation_pool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_pool_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_pool_list, 'to_alipay_dict'):
                params['operation_pool_list'] = self.operation_pool_list.to_alipay_dict()
            else:
                params['operation_pool_list'] = self.operation_pool_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingQipanCrowdoperationCreateModel()
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'operation_pool_list' in d:
            o.operation_pool_list = d['operation_pool_list']
        return o


