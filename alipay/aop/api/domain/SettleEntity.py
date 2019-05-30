#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleEntity(object):

    def __init__(self):
        self._settle_entity_id = None
        self._settle_entity_type = None

    @property
    def settle_entity_id(self):
        return self._settle_entity_id

    @settle_entity_id.setter
    def settle_entity_id(self, value):
        self._settle_entity_id = value
    @property
    def settle_entity_type(self):
        return self._settle_entity_type

    @settle_entity_type.setter
    def settle_entity_type(self, value):
        self._settle_entity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_entity_id:
            if hasattr(self.settle_entity_id, 'to_alipay_dict'):
                params['settle_entity_id'] = self.settle_entity_id.to_alipay_dict()
            else:
                params['settle_entity_id'] = self.settle_entity_id
        if self.settle_entity_type:
            if hasattr(self.settle_entity_type, 'to_alipay_dict'):
                params['settle_entity_type'] = self.settle_entity_type.to_alipay_dict()
            else:
                params['settle_entity_type'] = self.settle_entity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleEntity()
        if 'settle_entity_id' in d:
            o.settle_entity_id = d['settle_entity_id']
        if 'settle_entity_type' in d:
            o.settle_entity_type = d['settle_entity_type']
        return o


