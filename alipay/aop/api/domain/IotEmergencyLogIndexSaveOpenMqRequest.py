#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotEmergencyLogIndexSaveOpenMqRequest(object):

    def __init__(self):
        self._index_id = None
        self._value = None

    @property
    def index_id(self):
        return self._index_id

    @index_id.setter
    def index_id(self, value):
        self._index_id = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.index_id:
            if hasattr(self.index_id, 'to_alipay_dict'):
                params['index_id'] = self.index_id.to_alipay_dict()
            else:
                params['index_id'] = self.index_id
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotEmergencyLogIndexSaveOpenMqRequest()
        if 'index_id' in d:
            o.index_id = d['index_id']
        if 'value' in d:
            o.value = d['value']
        return o


