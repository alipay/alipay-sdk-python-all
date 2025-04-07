#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefForth(object):

    def __init__(self):
        self._object_string = None

    @property
    def object_string(self):
        return self._object_string

    @object_string.setter
    def object_string(self, value):
        self._object_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.object_string:
            if hasattr(self.object_string, 'to_alipay_dict'):
                params['object_string'] = self.object_string.to_alipay_dict()
            else:
                params['object_string'] = self.object_string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexRefForth()
        if 'object_string' in d:
            o.object_string = d['object_string']
        return o


