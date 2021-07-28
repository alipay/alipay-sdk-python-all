#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpOperationAuthAddModel(object):

    def __init__(self):
        self._auth_product_code = None
        self._merchant_no = None
        self._out_biz_no = None

    @property
    def auth_product_code(self):
        return self._auth_product_code

    @auth_product_code.setter
    def auth_product_code(self, value):
        self._auth_product_code = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_product_code:
            if hasattr(self.auth_product_code, 'to_alipay_dict'):
                params['auth_product_code'] = self.auth_product_code.to_alipay_dict()
            else:
                params['auth_product_code'] = self.auth_product_code
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpOperationAuthAddModel()
        if 'auth_product_code' in d:
            o.auth_product_code = d['auth_product_code']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


