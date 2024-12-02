#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeSchemasdktypeRainystestQueryModel(object):

    def __init__(self):
        self._demo = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSchemasdktypeRainystestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        return o


