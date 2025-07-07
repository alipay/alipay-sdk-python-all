#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpBusinesslocationQueryModel(object):

    def __init__(self):
        self._auth_id = None
        self._business_key = None
        self._product_code = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def business_key(self):
        return self._business_key

    @business_key.setter
    def business_key(self, value):
        self._business_key = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.business_key:
            if hasattr(self.business_key, 'to_alipay_dict'):
                params['business_key'] = self.business_key.to_alipay_dict()
            else:
                params['business_key'] = self.business_key
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpBusinesslocationQueryModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'business_key' in d:
            o.business_key = d['business_key']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


