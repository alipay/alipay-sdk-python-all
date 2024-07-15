#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuQueryParam(object):

    def __init__(self):
        self._product_id = None
        self._sku_id = None

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuQueryParam()
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


