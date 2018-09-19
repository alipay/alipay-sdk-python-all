#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandLevelInfo(object):

    def __init__(self):
        self._brand_code = None
        self._brand_level = None
        self._brand_name = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_level(self):
        return self._brand_level

    @brand_level.setter
    def brand_level(self, value):
        self._brand_level = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_level:
            if hasattr(self.brand_level, 'to_alipay_dict'):
                params['brand_level'] = self.brand_level.to_alipay_dict()
            else:
                params['brand_level'] = self.brand_level
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandLevelInfo()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_level' in d:
            o.brand_level = d['brand_level']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        return o


