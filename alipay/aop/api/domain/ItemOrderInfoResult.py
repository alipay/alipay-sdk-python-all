#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemOrderInfoResult(object):

    def __init__(self):
        self._image_url = None
        self._item_name = None
        self._merchant_item_link_page = None
        self._quantity = None
        self._unit_price = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def merchant_item_link_page(self):
        return self._merchant_item_link_page

    @merchant_item_link_page.setter
    def merchant_item_link_page(self, value):
        self._merchant_item_link_page = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.merchant_item_link_page:
            if hasattr(self.merchant_item_link_page, 'to_alipay_dict'):
                params['merchant_item_link_page'] = self.merchant_item_link_page.to_alipay_dict()
            else:
                params['merchant_item_link_page'] = self.merchant_item_link_page
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemOrderInfoResult()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'merchant_item_link_page' in d:
            o.merchant_item_link_page = d['merchant_item_link_page']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


