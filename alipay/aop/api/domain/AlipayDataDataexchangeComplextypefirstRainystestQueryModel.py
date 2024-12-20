#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class AlipayDataDataexchangeComplextypefirstRainystestQueryModel(object):

    def __init__(self):
        self._complex_type_01 = None
        self._complex_type_02 = None

    @property
    def complex_type_01(self):
        return self._complex_type_01

    @complex_type_01.setter
    def complex_type_01(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._complex_type_01 = value
        else:
            self._complex_type_01 = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def complex_type_02(self):
        return self._complex_type_02

    @complex_type_02.setter
    def complex_type_02(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._complex_type_02 = value
        else:
            self._complex_type_02 = RainyComplexTypesTheFirst.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.complex_type_01:
            if hasattr(self.complex_type_01, 'to_alipay_dict'):
                params['complex_type_01'] = self.complex_type_01.to_alipay_dict()
            else:
                params['complex_type_01'] = self.complex_type_01
        if self.complex_type_02:
            if hasattr(self.complex_type_02, 'to_alipay_dict'):
                params['complex_type_02'] = self.complex_type_02.to_alipay_dict()
            else:
                params['complex_type_02'] = self.complex_type_02
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeComplextypefirstRainystestQueryModel()
        if 'complex_type_01' in d:
            o.complex_type_01 = d['complex_type_01']
        if 'complex_type_02' in d:
            o.complex_type_02 = d['complex_type_02']
        return o


