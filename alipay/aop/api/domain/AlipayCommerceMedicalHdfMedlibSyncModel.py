#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfMedlibSyncModel(object):

    def __init__(self):
        self._data = None
        self._op = None
        self._type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def op(self):
        return self._op

    @op.setter
    def op(self, value):
        self._op = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.op:
            if hasattr(self.op, 'to_alipay_dict'):
                params['op'] = self.op.to_alipay_dict()
            else:
                params['op'] = self.op
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfMedlibSyncModel()
        if 'data' in d:
            o.data = d['data']
        if 'op' in d:
            o.op = d['op']
        if 'type' in d:
            o.type = d['type']
        return o


