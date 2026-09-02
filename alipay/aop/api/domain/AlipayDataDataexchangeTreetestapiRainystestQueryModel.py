#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeTreetestapiRainystestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_0521 = None
        self._demo_0525 = None

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
        return o


