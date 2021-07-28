#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StructureBrandInfo(object):

    def __init__(self):
        self._brand_en_name = None
        self._brand_logo = None
        self._brand_name = None

    @property
    def brand_en_name(self):
        return self._brand_en_name

    @brand_en_name.setter
    def brand_en_name(self, value):
        self._brand_en_name = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_en_name:
            if hasattr(self.brand_en_name, 'to_alipay_dict'):
                params['brand_en_name'] = self.brand_en_name.to_alipay_dict()
            else:
                params['brand_en_name'] = self.brand_en_name
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
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
        o = StructureBrandInfo()
        if 'brand_en_name' in d:
            o.brand_en_name = d['brand_en_name']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        return o


