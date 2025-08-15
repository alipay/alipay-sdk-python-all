#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysCompelxTypeWeakRefTwo(object):

    def __init__(self):
        self._demo_emtpy_prod_vv = None
        self._demo_weak_empty = None
        self._demo_weak_value = None

    @property
    def demo_emtpy_prod_vv(self):
        return self._demo_emtpy_prod_vv

    @demo_emtpy_prod_vv.setter
    def demo_emtpy_prod_vv(self, value):
        self._demo_emtpy_prod_vv = value
    @property
    def demo_weak_empty(self):
        return self._demo_weak_empty

    @demo_weak_empty.setter
    def demo_weak_empty(self, value):
        self._demo_weak_empty = value
    @property
    def demo_weak_value(self):
        return self._demo_weak_value

    @demo_weak_value.setter
    def demo_weak_value(self, value):
        self._demo_weak_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_emtpy_prod_vv:
            if hasattr(self.demo_emtpy_prod_vv, 'to_alipay_dict'):
                params['demo_emtpy_prod_vv'] = self.demo_emtpy_prod_vv.to_alipay_dict()
            else:
                params['demo_emtpy_prod_vv'] = self.demo_emtpy_prod_vv
        if self.demo_weak_empty:
            if hasattr(self.demo_weak_empty, 'to_alipay_dict'):
                params['demo_weak_empty'] = self.demo_weak_empty.to_alipay_dict()
            else:
                params['demo_weak_empty'] = self.demo_weak_empty
        if self.demo_weak_value:
            if hasattr(self.demo_weak_value, 'to_alipay_dict'):
                params['demo_weak_value'] = self.demo_weak_value.to_alipay_dict()
            else:
                params['demo_weak_value'] = self.demo_weak_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysCompelxTypeWeakRefTwo()
        if 'demo_emtpy_prod_vv' in d:
            o.demo_emtpy_prod_vv = d['demo_emtpy_prod_vv']
        if 'demo_weak_empty' in d:
            o.demo_weak_empty = d['demo_weak_empty']
        if 'demo_weak_value' in d:
            o.demo_weak_value = d['demo_weak_value']
        return o


