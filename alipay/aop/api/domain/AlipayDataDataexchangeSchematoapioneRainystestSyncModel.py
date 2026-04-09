#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst


class AlipayDataDataexchangeSchematoapioneRainystestSyncModel(object):

    def __init__(self):
        self._demo = None
        self._demo_open_id = None
        self._demo_ref = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_open_id(self):
        return self._demo_open_id

    @demo_open_id.setter
    def demo_open_id(self, value):
        self._demo_open_id = value
    @property
    def demo_ref(self):
        return self._demo_ref

    @demo_ref.setter
    def demo_ref(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._demo_ref = value
        else:
            self._demo_ref = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_open_id:
            if hasattr(self.demo_open_id, 'to_alipay_dict'):
                params['demo_open_id'] = self.demo_open_id.to_alipay_dict()
            else:
                params['demo_open_id'] = self.demo_open_id
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
        o = AlipayDataDataexchangeSchematoapioneRainystestSyncModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_open_id' in d:
            o.demo_open_id = d['demo_open_id']
        if 'demo_ref' in d:
            o.demo_ref = d['demo_ref']
        return o


