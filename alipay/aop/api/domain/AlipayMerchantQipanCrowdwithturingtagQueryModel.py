#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdOperationPool import CrowdOperationPool


class AlipayMerchantQipanCrowdwithturingtagQueryModel(object):

    def __init__(self):
        self._crowd_id = None
        self._crowd_pool_list = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_pool_list(self):
        return self._crowd_pool_list

    @crowd_pool_list.setter
    def crowd_pool_list(self, value):
        if isinstance(value, list):
            self._crowd_pool_list = list()
            for i in value:
                if isinstance(i, CrowdOperationPool):
                    self._crowd_pool_list.append(i)
                else:
                    self._crowd_pool_list.append(CrowdOperationPool.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.crowd_pool_list:
            if isinstance(self.crowd_pool_list, list):
                for i in range(0, len(self.crowd_pool_list)):
                    element = self.crowd_pool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_pool_list[i] = element.to_alipay_dict()
            if hasattr(self.crowd_pool_list, 'to_alipay_dict'):
                params['crowd_pool_list'] = self.crowd_pool_list.to_alipay_dict()
            else:
                params['crowd_pool_list'] = self.crowd_pool_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCrowdwithturingtagQueryModel()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'crowd_pool_list' in d:
            o.crowd_pool_list = d['crowd_pool_list']
        return o


