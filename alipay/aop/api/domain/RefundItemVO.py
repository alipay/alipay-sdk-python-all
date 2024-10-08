#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundItemVO(object):

    def __init__(self):
        self._amount_item = None
        self._app_item_code = None
        self._item_name = None
        self._price_original = None
        self._price_sale = None
        self._quantity_item = None
        self._sku_id = None

    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def app_item_code(self):
        return self._app_item_code

    @app_item_code.setter
    def app_item_code(self, value):
        self._app_item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def price_original(self):
        return self._price_original

    @price_original.setter
    def price_original(self, value):
        self._price_original = value
    @property
    def price_sale(self):
        return self._price_sale

    @price_sale.setter
    def price_sale(self, value):
        self._price_sale = value
    @property
    def quantity_item(self):
        return self._quantity_item

    @quantity_item.setter
    def quantity_item(self, value):
        self._quantity_item = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.app_item_code:
            if hasattr(self.app_item_code, 'to_alipay_dict'):
                params['app_item_code'] = self.app_item_code.to_alipay_dict()
            else:
                params['app_item_code'] = self.app_item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.price_original:
            if hasattr(self.price_original, 'to_alipay_dict'):
                params['price_original'] = self.price_original.to_alipay_dict()
            else:
                params['price_original'] = self.price_original
        if self.price_sale:
            if hasattr(self.price_sale, 'to_alipay_dict'):
                params['price_sale'] = self.price_sale.to_alipay_dict()
            else:
                params['price_sale'] = self.price_sale
        if self.quantity_item:
            if hasattr(self.quantity_item, 'to_alipay_dict'):
                params['quantity_item'] = self.quantity_item.to_alipay_dict()
            else:
                params['quantity_item'] = self.quantity_item
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
        o = RefundItemVO()
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'app_item_code' in d:
            o.app_item_code = d['app_item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'price_original' in d:
            o.price_original = d['price_original']
        if 'price_sale' in d:
            o.price_sale = d['price_sale']
        if 'quantity_item' in d:
            o.quantity_item = d['quantity_item']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


