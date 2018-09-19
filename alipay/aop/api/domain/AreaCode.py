#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AreaCode(object):

    def __init__(self):
        self._area_type = None
        self._code = None

    @property
    def area_type(self):
        return self._area_type

    @area_type.setter
    def area_type(self, value):
        self._area_type = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_type:
            if hasattr(self.area_type, 'to_alipay_dict'):
                params['area_type'] = self.area_type.to_alipay_dict()
            else:
                params['area_type'] = self.area_type
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AreaCode()
        if 'area_type' in d:
            o.area_type = d['area_type']
        if 'code' in d:
            o.code = d['code']
        return o


