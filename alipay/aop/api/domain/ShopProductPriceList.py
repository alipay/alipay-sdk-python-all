#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductList import ProductList


class ShopProductPriceList(object):

    def __init__(self):
        self._external_shop_id = None
        self._product_list = None
        self._shop_id = None

    @property
    def external_shop_id(self):
        return self._external_shop_id

    @external_shop_id.setter
    def external_shop_id(self, value):
        self._external_shop_id = value
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, ProductList):
                    self._product_list.append(i)
                else:
                    self._product_list.append(ProductList.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_shop_id:
            if hasattr(self.external_shop_id, 'to_alipay_dict'):
                params['external_shop_id'] = self.external_shop_id.to_alipay_dict()
            else:
                params['external_shop_id'] = self.external_shop_id
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopProductPriceList()
        if 'external_shop_id' in d:
            o.external_shop_id = d['external_shop_id']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


