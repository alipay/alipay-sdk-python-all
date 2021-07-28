#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RatioDetail(object):

    def __init__(self):
        self._area_code = None
        self._area_name = None
        self._id = None
        self._period = None
        self._ratio_label = None
        self._ratio_val = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def ratio_label(self):
        return self._ratio_label

    @ratio_label.setter
    def ratio_label(self, value):
        self._ratio_label = value
    @property
    def ratio_val(self):
        return self._ratio_val

    @ratio_val.setter
    def ratio_val(self, value):
        self._ratio_val = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.ratio_label:
            if hasattr(self.ratio_label, 'to_alipay_dict'):
                params['ratio_label'] = self.ratio_label.to_alipay_dict()
            else:
                params['ratio_label'] = self.ratio_label
        if self.ratio_val:
            if hasattr(self.ratio_val, 'to_alipay_dict'):
                params['ratio_val'] = self.ratio_val.to_alipay_dict()
            else:
                params['ratio_val'] = self.ratio_val
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RatioDetail()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'id' in d:
            o.id = d['id']
        if 'period' in d:
            o.period = d['period']
        if 'ratio_label' in d:
            o.ratio_label = d['ratio_label']
        if 'ratio_val' in d:
            o.ratio_val = d['ratio_val']
        return o


