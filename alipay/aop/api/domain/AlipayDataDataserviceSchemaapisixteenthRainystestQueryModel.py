#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainysComplexRefThird import RainysComplexRefThird
from alipay.aop.api.domain.RainyComplexTypesTheEighth import RainyComplexTypesTheEighth


class AlipayDataDataserviceSchemaapisixteenthRainystestQueryModel(object):

    def __init__(self):
        self._demo_object = None
        self._demo_weak = None

    @property
    def demo_object(self):
        return self._demo_object

    @demo_object.setter
    def demo_object(self, value):
        if isinstance(value, RainysComplexRefThird):
            self._demo_object = value
        else:
            self._demo_object = RainysComplexRefThird.from_alipay_dict(value)
    @property
    def demo_weak(self):
        return self._demo_weak

    @demo_weak.setter
    def demo_weak(self, value):
        if isinstance(value, RainyComplexTypesTheEighth):
            self._demo_weak = value
        else:
            self._demo_weak = RainyComplexTypesTheEighth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_object:
            if hasattr(self.demo_object, 'to_alipay_dict'):
                params['demo_object'] = self.demo_object.to_alipay_dict()
            else:
                params['demo_object'] = self.demo_object
        if self.demo_weak:
            if hasattr(self.demo_weak, 'to_alipay_dict'):
                params['demo_weak'] = self.demo_weak.to_alipay_dict()
            else:
                params['demo_weak'] = self.demo_weak
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapisixteenthRainystestQueryModel()
        if 'demo_object' in d:
            o.demo_object = d['demo_object']
        if 'demo_weak' in d:
            o.demo_weak = d['demo_weak']
        return o


