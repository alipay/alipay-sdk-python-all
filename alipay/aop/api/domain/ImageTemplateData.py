#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ImageTemplateData(object):

    def __init__(self):
        self._h = None
        self._i = None
        self._s = None
        self._w = None

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value
    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        self._i = value
    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value
    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value


    def to_alipay_dict(self):
        params = dict()
        if self.h:
            if hasattr(self.h, 'to_alipay_dict'):
                params['h'] = self.h.to_alipay_dict()
            else:
                params['h'] = self.h
        if self.i:
            if hasattr(self.i, 'to_alipay_dict'):
                params['i'] = self.i.to_alipay_dict()
            else:
                params['i'] = self.i
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        if self.w:
            if hasattr(self.w, 'to_alipay_dict'):
                params['w'] = self.w.to_alipay_dict()
            else:
                params['w'] = self.w
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ImageTemplateData()
        if 'h' in d:
            o.h = d['h']
        if 'i' in d:
            o.i = d['i']
        if 's' in d:
            o.s = d['s']
        if 'w' in d:
            o.w = d['w']
        return o


