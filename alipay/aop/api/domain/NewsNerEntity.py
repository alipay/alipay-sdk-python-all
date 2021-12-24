#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsNerEntity(object):

    def __init__(self):
        self._entity = None
        self._entity_type = None
        self._weight = None

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        self._entity = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity:
            if hasattr(self.entity, 'to_alipay_dict'):
                params['entity'] = self.entity.to_alipay_dict()
            else:
                params['entity'] = self.entity
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsNerEntity()
        if 'entity' in d:
            o.entity = d['entity']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'weight' in d:
            o.weight = d['weight']
        return o


