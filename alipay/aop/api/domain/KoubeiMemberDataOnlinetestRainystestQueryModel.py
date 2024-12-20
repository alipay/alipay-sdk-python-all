#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMemberDataOnlinetestRainystestQueryModel(object):

    def __init__(self):
        self._demo_case = None
        self._demo_cs = None
        self._demo_cs_2 = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
    @property
    def demo_cs(self):
        return self._demo_cs

    @demo_cs.setter
    def demo_cs(self, value):
        self._demo_cs = value
    @property
    def demo_cs_2(self):
        return self._demo_cs_2

    @demo_cs_2.setter
    def demo_cs_2(self, value):
        self._demo_cs_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        if self.demo_cs:
            if hasattr(self.demo_cs, 'to_alipay_dict'):
                params['demo_cs'] = self.demo_cs.to_alipay_dict()
            else:
                params['demo_cs'] = self.demo_cs
        if self.demo_cs_2:
            if hasattr(self.demo_cs_2, 'to_alipay_dict'):
                params['demo_cs_2'] = self.demo_cs_2.to_alipay_dict()
            else:
                params['demo_cs_2'] = self.demo_cs_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberDataOnlinetestRainystestQueryModel()
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        if 'demo_cs' in d:
            o.demo_cs = d['demo_cs']
        if 'demo_cs_2' in d:
            o.demo_cs_2 = d['demo_cs_2']
        return o


