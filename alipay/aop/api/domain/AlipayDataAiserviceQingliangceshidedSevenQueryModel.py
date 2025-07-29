#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceQingliangceshidedSevenQueryModel(object):

    def __init__(self):
        self._ceshi_demo = None

    @property
    def ceshi_demo(self):
        return self._ceshi_demo

    @ceshi_demo.setter
    def ceshi_demo(self, value):
        self._ceshi_demo = value


    def to_alipay_dict(self):
        params = dict()
        if self.ceshi_demo:
            if hasattr(self.ceshi_demo, 'to_alipay_dict'):
                params['ceshi_demo'] = self.ceshi_demo.to_alipay_dict()
            else:
                params['ceshi_demo'] = self.ceshi_demo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceQingliangceshidedSevenQueryModel()
        if 'ceshi_demo' in d:
            o.ceshi_demo = d['ceshi_demo']
        return o


