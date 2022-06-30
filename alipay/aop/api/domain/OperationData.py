#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationData(object):

    def __init__(self):
        self._operation_data = None
        self._operation_type = None

    @property
    def operation_data(self):
        return self._operation_data

    @operation_data.setter
    def operation_data(self, value):
        self._operation_data = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_data:
            if hasattr(self.operation_data, 'to_alipay_dict'):
                params['operation_data'] = self.operation_data.to_alipay_dict()
            else:
                params['operation_data'] = self.operation_data
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperationData()
        if 'operation_data' in d:
            o.operation_data = d['operation_data']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        return o


