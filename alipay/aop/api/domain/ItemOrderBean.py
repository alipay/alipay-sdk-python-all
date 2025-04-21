#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttributeBean import AttributeBean
from alipay.aop.api.domain.SideItemBean import SideItemBean


class ItemOrderBean(object):

    def __init__(self):
        self._amount = None
        self._attribute_list = None
        self._image_url = None
        self._item_id = None
        self._item_order_id = None
        self._name = None
        self._order_id = None
        self._original_price = None
        self._price = None
        self._quantity = None
        self._side_item_list = None
        self._sku_id = None
        self._snapshot_id = None
        self._spec_name = None
        self._spec_value = None
        self._thumbnail_url = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def attribute_list(self):
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, value):
        if isinstance(value, list):
            self._attribute_list = list()
            for i in value:
                if isinstance(i, AttributeBean):
                    self._attribute_list.append(i)
                else:
                    self._attribute_list.append(AttributeBean.from_alipay_dict(i))
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_order_id(self):
        return self._item_order_id

    @item_order_id.setter
    def item_order_id(self, value):
        self._item_order_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
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
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
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
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.attribute_list:
            if isinstance(self.attribute_list, list):
                for i in range(0, len(self.attribute_list)):
                    element = self.attribute_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attribute_list[i] = element.to_alipay_dict()
            if hasattr(self.attribute_list, 'to_alipay_dict'):
                params['attribute_list'] = self.attribute_list.to_alipay_dict()
            else:
                params['attribute_list'] = self.attribute_list
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_order_id:
            if hasattr(self.item_order_id, 'to_alipay_dict'):
                params['item_order_id'] = self.item_order_id.to_alipay_dict()
            else:
                params['item_order_id'] = self.item_order_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
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
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.snapshot_id:
            if hasattr(self.snapshot_id, 'to_alipay_dict'):
                params['snapshot_id'] = self.snapshot_id.to_alipay_dict()
            else:
                params['snapshot_id'] = self.snapshot_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemOrderBean()
        if 'amount' in d:
            o.amount = d['amount']
        if 'attribute_list' in d:
            o.attribute_list = d['attribute_list']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_order_id' in d:
            o.item_order_id = d['item_order_id']
        if 'name' in d:
            o.name = d['name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'side_item_list' in d:
            o.side_item_list = d['side_item_list']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'snapshot_id' in d:
            o.snapshot_id = d['snapshot_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'spec_value' in d:
            o.spec_value = d['spec_value']
        if 'thumbnail_url' in d:
            o.thumbnail_url = d['thumbnail_url']
        return o


