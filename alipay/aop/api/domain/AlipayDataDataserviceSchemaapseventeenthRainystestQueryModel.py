#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainysComplexRefFirst import RainysComplexRefFirst
from alipay.aop.api.domain.RainysComplexRefSecond import RainysComplexRefSecond


class AlipayDataDataserviceSchemaapseventeenthRainystestQueryModel(object):

    def __init__(self):
        self._demo_ref = None
        self._demo_weak_ref = None

    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainysComplexRefFirst):
            self._demo_ref = value
        else:
            self._demo_ref = RainysComplexRefFirst.from_alipay_dict(value)
    @property
    def demo_weak_ref(self):
        return self._demo_weak_ref

    @demo_weak_ref.setter
    def demo_weak_ref(self, value):
        if isinstance(value, RainysComplexRefSecond):
            self._demo_weak_ref = value
        else:
            self._demo_weak_ref = RainysComplexRefSecond.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_ref:
            if hasattr(self.demo_ref, 'to_alipay_dict'):
                params['demo_ref'] = self.demo_ref.to_alipay_dict()
            else:
                params['demo_ref'] = self.demo_ref
        if self.demo_weak_ref:
            if hasattr(self.demo_weak_ref, 'to_alipay_dict'):
                params['demo_weak_ref'] = self.demo_weak_ref.to_alipay_dict()
            else:
                params['demo_weak_ref'] = self.demo_weak_ref
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapseventeenthRainystestQueryModel()
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        if 'demo_weak_ref' in d:
            o.demo_weak_ref = d['demo_weak_ref']
        return o


