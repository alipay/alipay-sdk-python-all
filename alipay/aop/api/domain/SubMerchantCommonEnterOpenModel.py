#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubMerchantCommonEnterOpenModel(object):

    def __init__(self):
        self._extend_fields = None
        self._product_code = None
        self._s_short_name = None

    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, value):
        self._extend_fields = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def s_short_name(self):
        return self._s_short_name

    @s_short_name.setter
    def s_short_name(self, value):
        self._s_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_fields:
            if hasattr(self.extend_fields, 'to_alipay_dict'):
                params['extend_fields'] = self.extend_fields.to_alipay_dict()
            else:
                params['extend_fields'] = self.extend_fields
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.s_short_name:
            if hasattr(self.s_short_name, 'to_alipay_dict'):
                params['s_short_name'] = self.s_short_name.to_alipay_dict()
            else:
                params['s_short_name'] = self.s_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubMerchantCommonEnterOpenModel()
        if 'extend_fields' in d:
            o.extend_fields = d['extend_fields']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 's_short_name' in d:
            o.s_short_name = d['s_short_name']
        return o


