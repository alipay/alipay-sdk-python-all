#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtBrand(object):

    def __init__(self):
        self._brand_code = None
        self._name = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtBrand()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'name' in d:
            o.name = d['name']
        return o


