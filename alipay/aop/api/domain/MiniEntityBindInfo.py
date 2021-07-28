#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniContentPropertyInfo import MiniContentPropertyInfo


class MiniEntityBindInfo(object):

    def __init__(self):
        self._entity_id = None
        self._property_list = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def property_list(self):
        return self._property_list

    @property_list.setter
    def property_list(self, value):
        if isinstance(value, list):
            self._property_list = list()
            for i in value:
                if isinstance(i, MiniContentPropertyInfo):
                    self._property_list.append(i)
                else:
                    self._property_list.append(MiniContentPropertyInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.property_list:
            if isinstance(self.property_list, list):
                for i in range(0, len(self.property_list)):
                    element = self.property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_list[i] = element.to_alipay_dict()
            if hasattr(self.property_list, 'to_alipay_dict'):
                params['property_list'] = self.property_list.to_alipay_dict()
            else:
                params['property_list'] = self.property_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniEntityBindInfo()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'property_list' in d:
            o.property_list = d['property_list']
        return o


