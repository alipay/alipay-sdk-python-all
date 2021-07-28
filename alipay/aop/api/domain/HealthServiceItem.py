#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HealthServiceSku import HealthServiceSku
from alipay.aop.api.domain.HealthServiceSku import HealthServiceSku


class HealthServiceItem(object):

    def __init__(self):
        self._item_id = None
        self._item_name = None
        self._merchant_item_bar_code = None
        self._merchant_item_code = None
        self._price = None
        self._sku_list = None
        self._skus = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def merchant_item_bar_code(self):
        return self._merchant_item_bar_code

    @merchant_item_bar_code.setter
    def merchant_item_bar_code(self, value):
        self._merchant_item_bar_code = value
    @property
    def merchant_item_code(self):
        return self._merchant_item_code

    @merchant_item_code.setter
    def merchant_item_code(self, value):
        self._merchant_item_code = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, HealthServiceSku):
            self._sku_list = value
        else:
            self._sku_list = HealthServiceSku.from_alipay_dict(value)
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, HealthServiceSku):
                    self._skus.append(i)
                else:
                    self._skus.append(HealthServiceSku.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.merchant_item_bar_code:
            if hasattr(self.merchant_item_bar_code, 'to_alipay_dict'):
                params['merchant_item_bar_code'] = self.merchant_item_bar_code.to_alipay_dict()
            else:
                params['merchant_item_bar_code'] = self.merchant_item_bar_code
        if self.merchant_item_code:
            if hasattr(self.merchant_item_code, 'to_alipay_dict'):
                params['merchant_item_code'] = self.merchant_item_code.to_alipay_dict()
            else:
                params['merchant_item_code'] = self.merchant_item_code
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sku_list:
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthServiceItem()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'merchant_item_bar_code' in d:
            o.merchant_item_bar_code = d['merchant_item_bar_code']
        if 'merchant_item_code' in d:
            o.merchant_item_code = d['merchant_item_code']
        if 'price' in d:
            o.price = d['price']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        if 'skus' in d:
            o.skus = d['skus']
        return o


