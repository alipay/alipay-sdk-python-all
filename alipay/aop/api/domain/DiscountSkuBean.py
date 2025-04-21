#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountActivityBean import DiscountActivityBean
from alipay.aop.api.domain.InventoryBean import InventoryBean


class DiscountSkuBean(object):

    def __init__(self):
        self._activity = None
        self._inventory = None
        self._item_id = None
        self._price = None
        self._quantity = None
        self._sku_id = None
        self._spec_name = None
        self._spec_value = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, DiscountActivityBean):
            self._activity = value
        else:
            self._activity = DiscountActivityBean.from_alipay_dict(value)
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        if isinstance(value, InventoryBean):
            self._inventory = value
        else:
            self._inventory = InventoryBean.from_alipay_dict(value)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
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
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def spec_value(self):
        return self._spec_value

    @spec_value.setter
    def spec_value(self, value):
        self._spec_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
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
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.spec_value:
            if hasattr(self.spec_value, 'to_alipay_dict'):
                params['spec_value'] = self.spec_value.to_alipay_dict()
            else:
                params['spec_value'] = self.spec_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountSkuBean()
        if 'activity' in d:
            o.activity = d['activity']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'spec_value' in d:
            o.spec_value = d['spec_value']
        return o


