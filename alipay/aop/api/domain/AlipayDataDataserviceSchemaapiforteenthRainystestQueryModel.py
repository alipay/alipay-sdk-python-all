#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSchemaapiforteenthRainystestQueryModel(object):

    def __init__(self):
        self._demo_case = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapiforteenthRainystestQueryModel()
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        return o


