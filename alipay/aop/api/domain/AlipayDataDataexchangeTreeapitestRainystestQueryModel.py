#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataexchangeTreeapitestRainystestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_choice = None
        self._demo_sp = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_choice(self):
        return self._demo_choice

    @demo_choice.setter
    def demo_choice(self, value):
        self._demo_choice = value
    @property
    def demo_sp(self):
        return self._demo_sp

    @demo_sp.setter
    def demo_sp(self, value):
        self._demo_sp = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_choice:
            if hasattr(self.demo_choice, 'to_alipay_dict'):
                params['demo_choice'] = self.demo_choice.to_alipay_dict()
            else:
                params['demo_choice'] = self.demo_choice
        if self.demo_sp:
            if hasattr(self.demo_sp, 'to_alipay_dict'):
                params['demo_sp'] = self.demo_sp.to_alipay_dict()
            else:
                params['demo_sp'] = self.demo_sp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeTreeapitestRainystestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_choice' in d:
            o.demo_choice = d['demo_choice']
        if 'demo_sp' in d:
            o.demo_sp = d['demo_sp']
        return o


