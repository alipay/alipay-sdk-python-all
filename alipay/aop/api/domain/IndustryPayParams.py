#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryPayParams(object):

    def __init__(self):
        self._async_type = None

    @property
    def async_type(self):
        return self._async_type

    @async_type.setter
    def async_type(self, value):
        self._async_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_type:
            if hasattr(self.async_type, 'to_alipay_dict'):
                params['async_type'] = self.async_type.to_alipay_dict()
            else:
                params['async_type'] = self.async_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryPayParams()
        if 'async_type' in d:
            o.async_type = d['async_type']
        return o


