#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TextTemplateData(object):

    def __init__(self):
        self._m = None

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value):
        self._m = value


    def to_alipay_dict(self):
        params = dict()
        if self.m:
            if hasattr(self.m, 'to_alipay_dict'):
                params['m'] = self.m.to_alipay_dict()
            else:
                params['m'] = self.m
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TextTemplateData()
        if 'm' in d:
            o.m = d['m']
        return o


