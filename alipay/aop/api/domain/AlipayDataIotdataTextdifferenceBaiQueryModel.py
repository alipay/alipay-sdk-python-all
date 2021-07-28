#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataTextdifferenceBaiQueryModel(object):

    def __init__(self):
        self._text_s = None
        self._text_t = None

    @property
    def text_s(self):
        return self._text_s

    @text_s.setter
    def text_s(self, value):
        self._text_s = value
    @property
    def text_t(self):
        return self._text_t

    @text_t.setter
    def text_t(self, value):
        self._text_t = value


    def to_alipay_dict(self):
        params = dict()
        if self.text_s:
            if hasattr(self.text_s, 'to_alipay_dict'):
                params['text_s'] = self.text_s.to_alipay_dict()
            else:
                params['text_s'] = self.text_s
        if self.text_t:
            if hasattr(self.text_t, 'to_alipay_dict'):
                params['text_t'] = self.text_t.to_alipay_dict()
            else:
                params['text_t'] = self.text_t
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataTextdifferenceBaiQueryModel()
        if 'text_s' in d:
            o.text_s = d['text_s']
        if 'text_t' in d:
            o.text_t = d['text_t']
        return o


