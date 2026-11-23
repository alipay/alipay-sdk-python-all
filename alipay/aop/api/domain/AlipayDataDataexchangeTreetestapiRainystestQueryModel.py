#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst
from alipay.aop.api.domain.RainyComplexTypesTheSixth import RainyComplexTypesTheSixth


class AlipayDataDataexchangeTreetestapiRainystestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_0521 = None
        self._demo_0525 = None
        self._demo_firest_ref = None
        self._demo_ref = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_0521(self):
        return self._demo_0521

    @demo_0521.setter
    def demo_0521(self, value):
        self._demo_0521 = value
    @property
    def demo_0525(self):
        return self._demo_0525

    @demo_0525.setter
    def demo_0525(self, value):
        self._demo_0525 = value
    @property
    def demo_firest_ref(self):
        return self._demo_firest_ref

    @demo_firest_ref.setter
    def demo_firest_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._demo_firest_ref = value
        else:
            self._demo_firest_ref = RainyComplexTypesTheFirst.from_alipay_dict(value)
    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesTheSixth):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesTheSixth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_0521:
            if hasattr(self.demo_0521, 'to_alipay_dict'):
                params['demo_0521'] = self.demo_0521.to_alipay_dict()
            else:
                params['demo_0521'] = self.demo_0521
        if self.demo_0525:
            if hasattr(self.demo_0525, 'to_alipay_dict'):
                params['demo_0525'] = self.demo_0525.to_alipay_dict()
            else:
                params['demo_0525'] = self.demo_0525
        if self.demo_firest_ref:
            if hasattr(self.demo_firest_ref, 'to_alipay_dict'):
                params['demo_firest_ref'] = self.demo_firest_ref.to_alipay_dict()
            else:
                params['demo_firest_ref'] = self.demo_firest_ref
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
        o = AlipayDataDataexchangeTreetestapiRainystestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_0521' in d:
            o.demo_0521 = d['demo_0521']
        if 'demo_0525' in d:
            o.demo_0525 = d['demo_0525']
        if 'demo_firest_ref' in d:
            o.demo_firest_ref = d['demo_firest_ref']
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        return o


