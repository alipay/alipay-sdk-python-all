#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class RainyComplexTypesTheSixth(object):

    def __init__(self):
        self._complextype_01 = None

    @property
    def complextype_01(self):
        return self._complextype_01

    @complextype_01.setter
    def complextype_01(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._complextype_01 = value
        else:
            self._complextype_01 = RainyComplexTypesTheFourth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.complextype_01:
            if hasattr(self.complextype_01, 'to_alipay_dict'):
                params['complextype_01'] = self.complextype_01.to_alipay_dict()
            else:
                params['complextype_01'] = self.complextype_01
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheSixth()
        if 'complextype_01' in d:
            o.complextype_01 = d['complextype_01']
        return o


