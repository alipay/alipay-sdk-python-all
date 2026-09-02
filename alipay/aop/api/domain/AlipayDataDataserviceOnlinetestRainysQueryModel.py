#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheten import RainyComplexTypesTheten


class AlipayDataDataserviceOnlinetestRainysQueryModel(object):

    def __init__(self):
        self._demo_ref = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesTheten):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesTheten.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_ref:
            if hasattr(self.demo_ref, 'to_alipay_dict'):
                params['demo_ref'] = self.demo_ref.to_alipay_dict()
            else:
                params['demo_ref'] = self.demo_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceOnlinetestRainysQueryModel()
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        return o


