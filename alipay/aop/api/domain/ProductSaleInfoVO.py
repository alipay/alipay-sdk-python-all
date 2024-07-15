#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuSaleInfoVO import SkuSaleInfoVO


class ProductSaleInfoVO(object):

    def __init__(self):
        self._can_sell = None
        self._division_code = None
        self._fuzzy_quantity = None
        self._product_id = None
        self._product_status = None
        self._quantity = None
        self._shop_id = None
        self._skus = None
        self._title = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def fuzzy_quantity(self):
        return self._fuzzy_quantity

    @fuzzy_quantity.setter
    def fuzzy_quantity(self, value):
        self._fuzzy_quantity = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, SkuSaleInfoVO):
                    self._skus.append(i)
                else:
                    self._skus.append(SkuSaleInfoVO.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.fuzzy_quantity:
            if hasattr(self.fuzzy_quantity, 'to_alipay_dict'):
                params['fuzzy_quantity'] = self.fuzzy_quantity.to_alipay_dict()
            else:
                params['fuzzy_quantity'] = self.fuzzy_quantity
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_status:
            if hasattr(self.product_status, 'to_alipay_dict'):
                params['product_status'] = self.product_status.to_alipay_dict()
            else:
                params['product_status'] = self.product_status
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductSaleInfoVO()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'fuzzy_quantity' in d:
            o.fuzzy_quantity = d['fuzzy_quantity']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_status' in d:
            o.product_status = d['product_status']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'skus' in d:
            o.skus = d['skus']
        if 'title' in d:
            o.title = d['title']
        return o


