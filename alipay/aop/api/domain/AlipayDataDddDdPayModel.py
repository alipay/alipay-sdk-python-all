#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheten import RainyComplexTypesTheten


class AlipayDataDddDdPayModel(object):

    def __init__(self):
        self._dem_ref = None

    @property
    def dem_ref(self):
        return self._dem_ref

    @dem_ref.setter
    def dem_ref(self, value):
        if isinstance(value, RainyComplexTypesTheten):
            self._dem_ref = value
        else:
            self._dem_ref = RainyComplexTypesTheten.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.dem_ref:
            if hasattr(self.dem_ref, 'to_alipay_dict'):
                params['dem_ref'] = self.dem_ref.to_alipay_dict()
            else:
                params['dem_ref'] = self.dem_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDddDdPayModel()
        if 'dem_ref' in d:
            o.dem_ref = d['dem_ref']
        return o


