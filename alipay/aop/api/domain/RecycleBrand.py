#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleBrand(object):

    def __init__(self):
        self._brand_code = None
        self._brand_name = None
        self._brand_url = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_url(self):
        return self._brand_url

    @brand_url.setter
    def brand_url(self, value):
        self._brand_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_url:
            if hasattr(self.brand_url, 'to_alipay_dict'):
                params['brand_url'] = self.brand_url.to_alipay_dict()
            else:
                params['brand_url'] = self.brand_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleBrand()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_url' in d:
            o.brand_url = d['brand_url']
        return o


