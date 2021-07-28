#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemExtInfo import ItemExtInfo


class ItemSkuCreateInfo(object):

    def __init__(self):
        self._cost_price = None
        self._ext_info = None
        self._external_sku_id = None
        self._inventory = None
        self._original_price = None
        self._price = None

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, value):
        self._cost_price = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ItemExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ItemExtInfo.from_alipay_dict(i))
    @property
    def external_sku_id(self):
        return self._external_sku_id

    @external_sku_id.setter
    def external_sku_id(self, value):
        self._external_sku_id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.cost_price:
            if hasattr(self.cost_price, 'to_alipay_dict'):
                params['cost_price'] = self.cost_price.to_alipay_dict()
            else:
                params['cost_price'] = self.cost_price
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_sku_id:
            if hasattr(self.external_sku_id, 'to_alipay_dict'):
                params['external_sku_id'] = self.external_sku_id.to_alipay_dict()
            else:
                params['external_sku_id'] = self.external_sku_id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemSkuCreateInfo()
        if 'cost_price' in d:
            o.cost_price = d['cost_price']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_sku_id' in d:
            o.external_sku_id = d['external_sku_id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        return o


