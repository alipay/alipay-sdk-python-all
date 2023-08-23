#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubOrderContent(object):

    def __init__(self):
        self._discount_fee = None
        self._origin_fee = None
        self._pay_fee = None
        self._sale_price = None
        self._sale_quantity = None
        self._sku_id = None
        self._sub_title = None
        self._title = None
        self._title_img = None

    @property
    def discount_fee(self):
        return self._discount_fee

    @discount_fee.setter
    def discount_fee(self, value):
        self._discount_fee = value
    @property
    def origin_fee(self):
        return self._origin_fee

    @origin_fee.setter
    def origin_fee(self, value):
        self._origin_fee = value
    @property
    def pay_fee(self):
        return self._pay_fee

    @pay_fee.setter
    def pay_fee(self, value):
        self._pay_fee = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_quantity(self):
        return self._sale_quantity

    @sale_quantity.setter
    def sale_quantity(self, value):
        self._sale_quantity = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def title_img(self):
        return self._title_img

    @title_img.setter
    def title_img(self, value):
        self._title_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_fee:
            if hasattr(self.discount_fee, 'to_alipay_dict'):
                params['discount_fee'] = self.discount_fee.to_alipay_dict()
            else:
                params['discount_fee'] = self.discount_fee
        if self.origin_fee:
            if hasattr(self.origin_fee, 'to_alipay_dict'):
                params['origin_fee'] = self.origin_fee.to_alipay_dict()
            else:
                params['origin_fee'] = self.origin_fee
        if self.pay_fee:
            if hasattr(self.pay_fee, 'to_alipay_dict'):
                params['pay_fee'] = self.pay_fee.to_alipay_dict()
            else:
                params['pay_fee'] = self.pay_fee
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_quantity:
            if hasattr(self.sale_quantity, 'to_alipay_dict'):
                params['sale_quantity'] = self.sale_quantity.to_alipay_dict()
            else:
                params['sale_quantity'] = self.sale_quantity
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.title_img:
            if hasattr(self.title_img, 'to_alipay_dict'):
                params['title_img'] = self.title_img.to_alipay_dict()
            else:
                params['title_img'] = self.title_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubOrderContent()
        if 'discount_fee' in d:
            o.discount_fee = d['discount_fee']
        if 'origin_fee' in d:
            o.origin_fee = d['origin_fee']
        if 'pay_fee' in d:
            o.pay_fee = d['pay_fee']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_quantity' in d:
            o.sale_quantity = d['sale_quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'title_img' in d:
            o.title_img = d['title_img']
        return o


