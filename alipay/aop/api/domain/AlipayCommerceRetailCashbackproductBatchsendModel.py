#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailCashbackproductBatchsendModel(object):

    def __init__(self):
        self._operate_type = None
        self._products = None

    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = list()
            for i in value:
                self._products.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.products:
            if isinstance(self.products, list):
                for i in range(0, len(self.products)):
                    element = self.products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.products[i] = element.to_alipay_dict()
            if hasattr(self.products, 'to_alipay_dict'):
                params['products'] = self.products.to_alipay_dict()
            else:
                params['products'] = self.products
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackproductBatchsendModel()
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'products' in d:
            o.products = d['products']
        return o


