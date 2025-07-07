#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeSchemaapithirtyfouthRainstestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_case = None
        self._open_id = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSchemaapithirtyfouthRainstestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


