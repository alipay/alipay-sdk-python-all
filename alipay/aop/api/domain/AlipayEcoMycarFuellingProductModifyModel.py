#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Product import Product
from alipay.aop.api.domain.Sale import Sale


class AlipayEcoMycarFuellingProductModifyModel(object):

    def __init__(self):
        self._out_shop_id = None
        self._product = None
        self._sale = None
        self._shop_id = None

    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, list):
            self._product = list()
            for i in value:
                if isinstance(i, Product):
                    self._product.append(i)
                else:
                    self._product.append(Product.from_alipay_dict(i))
    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, value):
        if isinstance(value, list):
            self._sale = list()
            for i in value:
                if isinstance(i, Sale):
                    self._sale.append(i)
                else:
                    self._sale.append(Sale.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.product:
            if isinstance(self.product, list):
                for i in range(0, len(self.product)):
                    element = self.product[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product[i] = element.to_alipay_dict()
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.sale:
            if isinstance(self.sale, list):
                for i in range(0, len(self.sale)):
                    element = self.sale[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale[i] = element.to_alipay_dict()
            if hasattr(self.sale, 'to_alipay_dict'):
                params['sale'] = self.sale.to_alipay_dict()
            else:
                params['sale'] = self.sale
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
        o = AlipayEcoMycarFuellingProductModifyModel()
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'product' in d:
            o.product = d['product']
        if 'sale' in d:
            o.sale = d['sale']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


