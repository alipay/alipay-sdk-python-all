#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceTreeapitenthRainystestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_boolean = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_boolean(self):
        return self._demo_boolean

    @demo_boolean.setter
    def demo_boolean(self, value):
        self._demo_boolean = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_boolean:
            if hasattr(self.demo_boolean, 'to_alipay_dict'):
                params['demo_boolean'] = self.demo_boolean.to_alipay_dict()
            else:
                params['demo_boolean'] = self.demo_boolean
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceTreeapitenthRainystestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_boolean' in d:
            o.demo_boolean = d['demo_boolean']
        return o


