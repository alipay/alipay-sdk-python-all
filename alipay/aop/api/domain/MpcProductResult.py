#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcProductResult(object):

    def __init__(self):
        self._can_sell = None
        self._price = None
        self._product_id = None
        self._product_pic_url = None
        self._product_title = None
        self._purchaser_id = None
        self._quantity = None
        self._sku_id = None
        self._sku_title = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_pic_url(self):
        return self._product_pic_url

    @product_pic_url.setter
    def product_pic_url(self, value):
        self._product_pic_url = value
    @property
    def product_title(self):
        return self._product_title

    @product_title.setter
    def product_title(self, value):
        self._product_title = value
    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_title(self):
        return self._sku_title

    @sku_title.setter
    def sku_title(self, value):
        self._sku_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_pic_url:
            if hasattr(self.product_pic_url, 'to_alipay_dict'):
                params['product_pic_url'] = self.product_pic_url.to_alipay_dict()
            else:
                params['product_pic_url'] = self.product_pic_url
        if self.product_title:
            if hasattr(self.product_title, 'to_alipay_dict'):
                params['product_title'] = self.product_title.to_alipay_dict()
            else:
                params['product_title'] = self.product_title
        if self.purchaser_id:
            if hasattr(self.purchaser_id, 'to_alipay_dict'):
                params['purchaser_id'] = self.purchaser_id.to_alipay_dict()
            else:
                params['purchaser_id'] = self.purchaser_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_title:
            if hasattr(self.sku_title, 'to_alipay_dict'):
                params['sku_title'] = self.sku_title.to_alipay_dict()
            else:
                params['sku_title'] = self.sku_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcProductResult()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'price' in d:
            o.price = d['price']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_pic_url' in d:
            o.product_pic_url = d['product_pic_url']
        if 'product_title' in d:
            o.product_title = d['product_title']
        if 'purchaser_id' in d:
            o.purchaser_id = d['purchaser_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_title' in d:
            o.sku_title = d['sku_title']
        return o


