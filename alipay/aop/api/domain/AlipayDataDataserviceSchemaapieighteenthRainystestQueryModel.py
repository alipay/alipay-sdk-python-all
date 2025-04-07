#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainysComplexRefForth import RainysComplexRefForth
from alipay.aop.api.domain.RainysComplexRefFifth import RainysComplexRefFifth


class AlipayDataDataserviceSchemaapieighteenthRainystestQueryModel(object):

    def __init__(self):
        self._demo_object_1 = None
        self._demo_weak = None

    @property
    def demo_object_1(self):
        return self._demo_object_1

    @demo_object_1.setter
    def demo_object_1(self, value):
        if isinstance(value, RainysComplexRefForth):
            self._demo_object_1 = value
        else:
            self._demo_object_1 = RainysComplexRefForth.from_alipay_dict(value)
    @property
    def demo_weak(self):
        return self._demo_weak

    @demo_weak.setter
    def demo_weak(self, value):
        if isinstance(value, RainysComplexRefFifth):
            self._demo_weak = value
        else:
            self._demo_weak = RainysComplexRefFifth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_object_1:
            if hasattr(self.demo_object_1, 'to_alipay_dict'):
                params['demo_object_1'] = self.demo_object_1.to_alipay_dict()
            else:
                params['demo_object_1'] = self.demo_object_1
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
        o = AlipayDataDataserviceSchemaapieighteenthRainystestQueryModel()
        if 'demo_object_1' in d:
            o.demo_object_1 = d['demo_object_1']
        if 'demo_weak' in d:
            o.demo_weak = d['demo_weak']
        return o


