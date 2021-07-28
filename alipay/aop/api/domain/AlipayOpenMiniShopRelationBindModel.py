#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniEntityBindInfo import MiniEntityBindInfo


class AlipayOpenMiniShopRelationBindModel(object):

    def __init__(self):
        self._entity_info = None
        self._operation = None

    @property
    def entity_info(self):
        return self._entity_info

    @entity_info.setter
    def entity_info(self, value):
        if isinstance(value, list):
            self._entity_info = list()
            for i in value:
                if isinstance(i, MiniEntityBindInfo):
                    self._entity_info.append(i)
                else:
                    self._entity_info.append(MiniEntityBindInfo.from_alipay_dict(i))
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_info:
            if isinstance(self.entity_info, list):
                for i in range(0, len(self.entity_info)):
                    element = self.entity_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_info[i] = element.to_alipay_dict()
            if hasattr(self.entity_info, 'to_alipay_dict'):
                params['entity_info'] = self.entity_info.to_alipay_dict()
            else:
                params['entity_info'] = self.entity_info
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniShopRelationBindModel()
        if 'entity_info' in d:
            o.entity_info = d['entity_info']
        if 'operation' in d:
            o.operation = d['operation']
        return o


