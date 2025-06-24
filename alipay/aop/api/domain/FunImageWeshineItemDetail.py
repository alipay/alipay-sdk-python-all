#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FunImageWeshineItemDetail(object):

    def __init__(self):
        self._gif = None
        self._h = None
        self._w = None
        self._webp = None

    @property
    def gif(self):
        return self._gif

    @gif.setter
    def gif(self, value):
        self._gif = value
    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value
    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value
    @property
    def webp(self):
        return self._webp

    @webp.setter
    def webp(self, value):
        self._webp = value


    def to_alipay_dict(self):
        params = dict()
        if self.gif:
            if hasattr(self.gif, 'to_alipay_dict'):
                params['gif'] = self.gif.to_alipay_dict()
            else:
                params['gif'] = self.gif
        if self.h:
            if hasattr(self.h, 'to_alipay_dict'):
                params['h'] = self.h.to_alipay_dict()
            else:
                params['h'] = self.h
        if self.w:
            if hasattr(self.w, 'to_alipay_dict'):
                params['w'] = self.w.to_alipay_dict()
            else:
                params['w'] = self.w
        if self.webp:
            if hasattr(self.webp, 'to_alipay_dict'):
                params['webp'] = self.webp.to_alipay_dict()
            else:
                params['webp'] = self.webp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FunImageWeshineItemDetail()
        if 'gif' in d:
            o.gif = d['gif']
        if 'h' in d:
            o.h = d['h']
        if 'w' in d:
            o.w = d['w']
        if 'webp' in d:
            o.webp = d['webp']
        return o


