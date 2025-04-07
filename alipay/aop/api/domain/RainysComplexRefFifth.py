#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefFifth(object):

    def __init__(self):
        self._param_demo = None

    @property
    def param_demo(self):
        return self._param_demo

    @param_demo.setter
    def param_demo(self, value):
        self._param_demo = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_demo:
            if hasattr(self.param_demo, 'to_alipay_dict'):
                params['param_demo'] = self.param_demo.to_alipay_dict()
            else:
                params['param_demo'] = self.param_demo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexRefFifth()
        if 'param_demo' in d:
            o.param_demo = d['param_demo']
        return o


