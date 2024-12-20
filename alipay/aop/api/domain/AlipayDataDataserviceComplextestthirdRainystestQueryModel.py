#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceComplextestthirdRainystestQueryModel(object):

    def __init__(self):
        self._complex_type = None

    @property
    def complex_type(self):
        return self._complex_type

    @complex_type.setter
    def complex_type(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._complex_type = value
        else:
            self._complex_type = RainyComplexTypesTheFourth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.complex_type:
            if hasattr(self.complex_type, 'to_alipay_dict'):
                params['complex_type'] = self.complex_type.to_alipay_dict()
            else:
                params['complex_type'] = self.complex_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceComplextestthirdRainystestQueryModel()
        if 'complex_type' in d:
            o.complex_type = d['complex_type']
        return o


