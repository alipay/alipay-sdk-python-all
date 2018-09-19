#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOffilneProduct(object):

    def __init__(self):
        self._biz_data = None
        self._prod_code = None
        self._prod_name = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOffilneProduct()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        return o


