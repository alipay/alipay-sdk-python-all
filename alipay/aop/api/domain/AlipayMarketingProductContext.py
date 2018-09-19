#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingProductContext(object):

    def __init__(self):
        self._client_id = None
        self._product = None
        self._product_version = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        self._product_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.product_version:
            if hasattr(self.product_version, 'to_alipay_dict'):
                params['product_version'] = self.product_version.to_alipay_dict()
            else:
                params['product_version'] = self.product_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingProductContext()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'product' in d:
            o.product = d['product']
        if 'product_version' in d:
            o.product_version = d['product_version']
        return o


