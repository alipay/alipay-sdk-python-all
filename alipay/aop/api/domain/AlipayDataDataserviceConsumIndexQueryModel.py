#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceConsumIndexQueryModel(object):

    def __init__(self):
        self._area_code = None
        self._area_type = None
        self._category = None
        self._data_type = None
        self._period = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceConsumIndexQueryModel()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'category' in d:
            o.category = d['category']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'period' in d:
            o.period = d['period']
        return o


