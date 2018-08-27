#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppSmsgDataSyncModel(object):

    def __init__(self):
        self._data_one = None
        self._data_two = None

    @property
    def data_one(self):
        return self._data_one

    @data_one.setter
    def data_one(self, value):
        self._data_one = value
    @property
    def data_two(self):
        return self._data_two

    @data_two.setter
    def data_two(self, value):
        self._data_two = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_one:
            if hasattr(self.data_one, 'to_alipay_dict'):
                params['data_one'] = self.data_one.to_alipay_dict()
            else:
                params['data_one'] = self.data_one
        if self.data_two:
            if hasattr(self.data_two, 'to_alipay_dict'):
                params['data_two'] = self.data_two.to_alipay_dict()
            else:
                params['data_two'] = self.data_two
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppSmsgDataSyncModel()
        if 'data_one' in d:
            o.data_one = d['data_one']
        if 'data_two' in d:
            o.data_two = d['data_two']
        return o


