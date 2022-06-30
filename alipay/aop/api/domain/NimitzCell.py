#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NimitzCell(object):

    def __init__(self):
        self._b_val = None
        self._d_val = None
        self._i_64_val = None
        self._s_val = None

    @property
    def b_val(self):
        return self._b_val

    @b_val.setter
    def b_val(self, value):
        self._b_val = value
    @property
    def d_val(self):
        return self._d_val

    @d_val.setter
    def d_val(self, value):
        self._d_val = value
    @property
    def i_64_val(self):
        return self._i_64_val

    @i_64_val.setter
    def i_64_val(self, value):
        self._i_64_val = value
    @property
    def s_val(self):
        return self._s_val

    @s_val.setter
    def s_val(self, value):
        self._s_val = value


    def to_alipay_dict(self):
        params = dict()
        if self.b_val:
            if hasattr(self.b_val, 'to_alipay_dict'):
                params['b_val'] = self.b_val.to_alipay_dict()
            else:
                params['b_val'] = self.b_val
        if self.d_val:
            if hasattr(self.d_val, 'to_alipay_dict'):
                params['d_val'] = self.d_val.to_alipay_dict()
            else:
                params['d_val'] = self.d_val
        if self.i_64_val:
            if hasattr(self.i_64_val, 'to_alipay_dict'):
                params['i_64_val'] = self.i_64_val.to_alipay_dict()
            else:
                params['i_64_val'] = self.i_64_val
        if self.s_val:
            if hasattr(self.s_val, 'to_alipay_dict'):
                params['s_val'] = self.s_val.to_alipay_dict()
            else:
                params['s_val'] = self.s_val
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NimitzCell()
        if 'b_val' in d:
            o.b_val = d['b_val']
        if 'd_val' in d:
            o.d_val = d['d_val']
        if 'i_64_val' in d:
            o.i_64_val = d['i_64_val']
        if 's_val' in d:
            o.s_val = d['s_val']
        return o


