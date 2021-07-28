#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceRecordFile(object):

    def __init__(self):
        self._records_type = None
        self._records_value = None

    @property
    def records_type(self):
        return self._records_type

    @records_type.setter
    def records_type(self, value):
        self._records_type = value
    @property
    def records_value(self):
        return self._records_value

    @records_value.setter
    def records_value(self, value):
        self._records_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.records_type:
            if hasattr(self.records_type, 'to_alipay_dict'):
                params['records_type'] = self.records_type.to_alipay_dict()
            else:
                params['records_type'] = self.records_type
        if self.records_value:
            if hasattr(self.records_value, 'to_alipay_dict'):
                params['records_value'] = self.records_value.to_alipay_dict()
            else:
                params['records_value'] = self.records_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceRecordFile()
        if 'records_type' in d:
            o.records_type = d['records_type']
        if 'records_value' in d:
            o.records_value = d['records_value']
        return o


