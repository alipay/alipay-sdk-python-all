#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefThird(object):

    def __init__(self):
        self._ob_num = None
        self._object_string = None

    @property
    def ob_num(self):
        return self._ob_num

    @ob_num.setter
    def ob_num(self, value):
        self._ob_num = value
    @property
    def object_string(self):
        return self._object_string

    @object_string.setter
    def object_string(self, value):
        self._object_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.ob_num:
            if hasattr(self.ob_num, 'to_alipay_dict'):
                params['ob_num'] = self.ob_num.to_alipay_dict()
            else:
                params['ob_num'] = self.ob_num
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
        o = RainysComplexRefThird()
        if 'ob_num' in d:
            o.ob_num = d['ob_num']
        if 'object_string' in d:
            o.object_string = d['object_string']
        return o


