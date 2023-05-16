#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcDistrictQueryModel(object):

    def __init__(self):
        self._area_level = None
        self._parent_code = None

    @property
    def area_level(self):
        return self._area_level

    @area_level.setter
    def area_level(self, value):
        self._area_level = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_level:
            if hasattr(self.area_level, 'to_alipay_dict'):
                params['area_level'] = self.area_level.to_alipay_dict()
            else:
                params['area_level'] = self.area_level
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcDistrictQueryModel()
        if 'area_level' in d:
            o.area_level = d['area_level']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        return o


