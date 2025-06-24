#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheThirteen import RainyComplexTypesTheThirteen


class AlipayDataDataserviceSchemthirtyfifthRainystestQueryModel(object):

    def __init__(self):
        self._demo_ref = None
        self._demo_str_1 = None
        self._demo_str_2 = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesTheThirteen):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesTheThirteen.from_alipay_dict(value)
    @property
    def demo_str_1(self):
        return self._demo_str_1

    @demo_str_1.setter
    def demo_str_1(self, value):
        self._demo_str_1 = value
    @property
    def demo_str_2(self):
        return self._demo_str_2

    @demo_str_2.setter
    def demo_str_2(self, value):
        self._demo_str_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_ref:
            if hasattr(self.demo_ref, 'to_alipay_dict'):
                params['demo_ref'] = self.demo_ref.to_alipay_dict()
            else:
                params['demo_ref'] = self.demo_ref
        if self.demo_str_1:
            if hasattr(self.demo_str_1, 'to_alipay_dict'):
                params['demo_str_1'] = self.demo_str_1.to_alipay_dict()
            else:
                params['demo_str_1'] = self.demo_str_1
        if self.demo_str_2:
            if hasattr(self.demo_str_2, 'to_alipay_dict'):
                params['demo_str_2'] = self.demo_str_2.to_alipay_dict()
            else:
                params['demo_str_2'] = self.demo_str_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemthirtyfifthRainystestQueryModel()
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        if 'demo_str_1' in d:
            o.demo_str_1 = d['demo_str_1']
        if 'demo_str_2' in d:
            o.demo_str_2 = d['demo_str_2']
        return o


