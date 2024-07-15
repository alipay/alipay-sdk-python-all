#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySolutionRecord(object):

    def __init__(self):
        self._data_key = None
        self._data_value = None

    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def data_value(self):
        return self._data_value

    @data_value.setter
    def data_value(self, value):
        self._data_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.data_value:
            if hasattr(self.data_value, 'to_alipay_dict'):
                params['data_value'] = self.data_value.to_alipay_dict()
            else:
                params['data_value'] = self.data_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySolutionRecord()
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'data_value' in d:
            o.data_value = d['data_value']
        return o


