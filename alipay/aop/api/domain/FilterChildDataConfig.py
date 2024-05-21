#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FilterChildDataConfig(object):

    def __init__(self):
        self._param = None
        self._text = None

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FilterChildDataConfig()
        if 'param' in d:
            o.param = d['param']
        if 'text' in d:
            o.text = d['text']
        return o


