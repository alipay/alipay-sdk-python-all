#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniDataVisitQueryModel(object):

    def __init__(self):
        self._data_scope = None
        self._province_code = None

    @property
    def data_scope(self):
        return self._data_scope

    @data_scope.setter
    def data_scope(self, value):
        self._data_scope = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_scope:
            if hasattr(self.data_scope, 'to_alipay_dict'):
                params['data_scope'] = self.data_scope.to_alipay_dict()
            else:
                params['data_scope'] = self.data_scope
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniDataVisitQueryModel()
        if 'data_scope' in d:
            o.data_scope = d['data_scope']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


