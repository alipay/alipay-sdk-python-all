#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSchemaapiseventhRainystestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_price = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_price(self):
        return self._demo_price

    @demo_price.setter
    def demo_price(self, value):
        self._demo_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_price:
            if hasattr(self.demo_price, 'to_alipay_dict'):
                params['demo_price'] = self.demo_price.to_alipay_dict()
            else:
                params['demo_price'] = self.demo_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapiseventhRainystestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_price' in d:
            o.demo_price = d['demo_price']
        return o


