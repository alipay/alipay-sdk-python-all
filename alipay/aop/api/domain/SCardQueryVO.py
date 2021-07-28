#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SCardQueryVO(object):

    def __init__(self):
        self._back_img = None
        self._item_amount = None
        self._item_id = None
        self._name = None
        self._sale_price = None

    @property
    def back_img(self):
        return self._back_img

    @back_img.setter
    def back_img(self, value):
        self._back_img = value
    @property
    def item_amount(self):
        return self._item_amount

    @item_amount.setter
    def item_amount(self, value):
        self._item_amount = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_img:
            if hasattr(self.back_img, 'to_alipay_dict'):
                params['back_img'] = self.back_img.to_alipay_dict()
            else:
                params['back_img'] = self.back_img
        if self.item_amount:
            if hasattr(self.item_amount, 'to_alipay_dict'):
                params['item_amount'] = self.item_amount.to_alipay_dict()
            else:
                params['item_amount'] = self.item_amount
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SCardQueryVO()
        if 'back_img' in d:
            o.back_img = d['back_img']
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'name' in d:
            o.name = d['name']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o


