#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTrainStagecaterelationQueryModel(object):

    def __init__(self):
        self._product_code = None
        self._sub_product_code = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_product_code(self):
        return self._sub_product_code

    @sub_product_code.setter
    def sub_product_code(self, value):
        self._sub_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_product_code:
            if hasattr(self.sub_product_code, 'to_alipay_dict'):
                params['sub_product_code'] = self.sub_product_code.to_alipay_dict()
            else:
                params['sub_product_code'] = self.sub_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainStagecaterelationQueryModel()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_product_code' in d:
            o.sub_product_code = d['sub_product_code']
        return o


