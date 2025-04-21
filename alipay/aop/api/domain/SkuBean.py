#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CartActivityBean import CartActivityBean
from alipay.aop.api.domain.AttributeBean import AttributeBean
from alipay.aop.api.domain.SideItemBean import SideItemBean
from alipay.aop.api.domain.AttributeBean import AttributeBean


class SkuBean(object):

    def __init__(self):
        self._activity = None
        self._add_time = None
        self._amount = None
        self._attr_desc = None
        self._inventory = None
        self._item_attribute_list = None
        self._item_id = None
        self._item_name = None
        self._original_price = None
        self._payment_price = None
        self._price = None
        self._quantity = None
        self._show_amt = None
        self._side_item_list = None
        self._sku_attribute_list = None
        self._sku_id = None
        self._spec_name = None
        self._spec_value = None
        self._thumbnail_url = None
        self._unit_amount = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, CartActivityBean):
            self._activity = value
        else:
            self._activity = CartActivityBean.from_alipay_dict(value)
    @property
    def add_time(self):
        return self._add_time

    @add_time.setter
    def add_time(self, value):
        self._add_time = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def attr_desc(self):
        return self._attr_desc

    @attr_desc.setter
    def attr_desc(self, value):
        self._attr_desc = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_attribute_list(self):
        return self._item_attribute_list

    @item_attribute_list.setter
    def item_attribute_list(self, value):
        if isinstance(value, list):
            self._item_attribute_list = list()
            for i in value:
                if isinstance(i, AttributeBean):
                    self._item_attribute_list.append(i)
                else:
                    self._item_attribute_list.append(AttributeBean.from_alipay_dict(i))
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
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def payment_price(self):
        return self._payment_price

    @payment_price.setter
    def payment_price(self, value):
        self._payment_price = value
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
    def show_amt(self):
        return self._show_amt

    @show_amt.setter
    def show_amt(self, value):
        self._show_amt = value
    @property
    def side_item_list(self):
        return self._side_item_list

    @side_item_list.setter
    def side_item_list(self, value):
        if isinstance(value, list):
            self._side_item_list = list()
            for i in value:
                if isinstance(i, SideItemBean):
                    self._side_item_list.append(i)
                else:
                    self._side_item_list.append(SideItemBean.from_alipay_dict(i))
    @property
    def sku_attribute_list(self):
        return self._sku_attribute_list

    @sku_attribute_list.setter
    def sku_attribute_list(self, value):
        if isinstance(value, list):
            self._sku_attribute_list = list()
            for i in value:
                if isinstance(i, AttributeBean):
                    self._sku_attribute_list.append(i)
                else:
                    self._sku_attribute_list.append(AttributeBean.from_alipay_dict(i))
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
    @property
    def thumbnail_url(self):
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        self._thumbnail_url = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity:
            if hasattr(self.activity, 'to_alipay_dict'):
                params['activity'] = self.activity.to_alipay_dict()
            else:
                params['activity'] = self.activity
        if self.add_time:
            if hasattr(self.add_time, 'to_alipay_dict'):
                params['add_time'] = self.add_time.to_alipay_dict()
            else:
                params['add_time'] = self.add_time
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.attr_desc:
            if hasattr(self.attr_desc, 'to_alipay_dict'):
                params['attr_desc'] = self.attr_desc.to_alipay_dict()
            else:
                params['attr_desc'] = self.attr_desc
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_attribute_list:
            if isinstance(self.item_attribute_list, list):
                for i in range(0, len(self.item_attribute_list)):
                    element = self.item_attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.item_attribute_list, 'to_alipay_dict'):
                params['item_attribute_list'] = self.item_attribute_list.to_alipay_dict()
            else:
                params['item_attribute_list'] = self.item_attribute_list
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
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.payment_price:
            if hasattr(self.payment_price, 'to_alipay_dict'):
                params['payment_price'] = self.payment_price.to_alipay_dict()
            else:
                params['payment_price'] = self.payment_price
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
        if self.show_amt:
            if hasattr(self.show_amt, 'to_alipay_dict'):
                params['show_amt'] = self.show_amt.to_alipay_dict()
            else:
                params['show_amt'] = self.show_amt
        if self.side_item_list:
            if isinstance(self.side_item_list, list):
                for i in range(0, len(self.side_item_list)):
                    element = self.side_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.side_item_list[i] = element.to_alipay_dict()
            if hasattr(self.side_item_list, 'to_alipay_dict'):
                params['side_item_list'] = self.side_item_list.to_alipay_dict()
            else:
                params['side_item_list'] = self.side_item_list
        if self.sku_attribute_list:
            if isinstance(self.sku_attribute_list, list):
                for i in range(0, len(self.sku_attribute_list)):
                    element = self.sku_attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_attribute_list, 'to_alipay_dict'):
                params['sku_attribute_list'] = self.sku_attribute_list.to_alipay_dict()
            else:
                params['sku_attribute_list'] = self.sku_attribute_list
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
        if self.thumbnail_url:
            if hasattr(self.thumbnail_url, 'to_alipay_dict'):
                params['thumbnail_url'] = self.thumbnail_url.to_alipay_dict()
            else:
                params['thumbnail_url'] = self.thumbnail_url
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuBean()
        if 'activity' in d:
            o.activity = d['activity']
        if 'add_time' in d:
            o.add_time = d['add_time']
        if 'amount' in d:
            o.amount = d['amount']
        if 'attr_desc' in d:
            o.attr_desc = d['attr_desc']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_attribute_list' in d:
            o.item_attribute_list = d['item_attribute_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'payment_price' in d:
            o.payment_price = d['payment_price']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'show_amt' in d:
            o.show_amt = d['show_amt']
        if 'side_item_list' in d:
            o.side_item_list = d['side_item_list']
        if 'sku_attribute_list' in d:
            o.sku_attribute_list = d['sku_attribute_list']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'spec_value' in d:
            o.spec_value = d['spec_value']
        if 'thumbnail_url' in d:
            o.thumbnail_url = d['thumbnail_url']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o


