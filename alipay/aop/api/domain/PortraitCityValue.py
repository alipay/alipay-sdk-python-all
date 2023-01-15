#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortraitCityValue(object):

    def __init__(self):
        self._area_code = None
        self._num = None
        self._portrait_value = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def portrait_value(self):
        return self._portrait_value

    @portrait_value.setter
    def portrait_value(self, value):
        self._portrait_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.portrait_value:
            if hasattr(self.portrait_value, 'to_alipay_dict'):
                params['portrait_value'] = self.portrait_value.to_alipay_dict()
            else:
                params['portrait_value'] = self.portrait_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitCityValue()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'num' in d:
            o.num = d['num']
        if 'portrait_value' in d:
            o.portrait_value = d['portrait_value']
        return o


