#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsitutionServicePreviewModel(object):

    def __init__(self):
        self._data_dt = None
        self._indicator_type = None

    @property
    def data_dt(self):
        return self._data_dt

    @data_dt.setter
    def data_dt(self, value):
        self._data_dt = value
    @property
    def indicator_type(self):
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, value):
        self._indicator_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_dt:
            if hasattr(self.data_dt, 'to_alipay_dict'):
                params['data_dt'] = self.data_dt.to_alipay_dict()
            else:
                params['data_dt'] = self.data_dt
        if self.indicator_type:
            if hasattr(self.indicator_type, 'to_alipay_dict'):
                params['indicator_type'] = self.indicator_type.to_alipay_dict()
            else:
                params['indicator_type'] = self.indicator_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsitutionServicePreviewModel()
        if 'data_dt' in d:
            o.data_dt = d['data_dt']
        if 'indicator_type' in d:
            o.indicator_type = d['indicator_type']
        return o


