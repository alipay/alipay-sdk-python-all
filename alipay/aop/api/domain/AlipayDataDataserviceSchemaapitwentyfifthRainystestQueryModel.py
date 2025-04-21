#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSchemaapitwentyfifthRainystestQueryModel(object):

    def __init__(self):
        self._demo_num = None

    @property
    def demo_num(self):
        return self._demo_num

    @demo_num.setter
    def demo_num(self, value):
        self._demo_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_num:
            if hasattr(self.demo_num, 'to_alipay_dict'):
                params['demo_num'] = self.demo_num.to_alipay_dict()
            else:
                params['demo_num'] = self.demo_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchemaapitwentyfifthRainystestQueryModel()
        if 'demo_num' in d:
            o.demo_num = d['demo_num']
        return o


