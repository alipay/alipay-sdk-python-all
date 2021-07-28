#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceMylogisticfinsysMessagePublishModel(object):

    def __init__(self):
        self._data = None
        self._method_name = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.method_name:
            if hasattr(self.method_name, 'to_alipay_dict'):
                params['method_name'] = self.method_name.to_alipay_dict()
            else:
                params['method_name'] = self.method_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceMylogisticfinsysMessagePublishModel()
        if 'data' in d:
            o.data = d['data']
        if 'method_name' in d:
            o.method_name = d['method_name']
        return o


