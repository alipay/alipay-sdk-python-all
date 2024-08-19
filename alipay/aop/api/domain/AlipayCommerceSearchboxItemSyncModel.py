#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSearchboxItemSyncModel(object):

    def __init__(self):
        self._category_id = None
        self._item_desc = None
        self._item_id = None
        self._item_image = None
        self._item_name = None
        self._item_order = None
        self._item_title = None
        self._item_url = None
        self._original_price = None
        self._price = None
        self._price_unit = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_image(self):
        return self._item_image

    @item_image.setter
    def item_image(self, value):
        self._item_image = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_order(self):
        return self._item_order

    @item_order.setter
    def item_order(self, value):
        self._item_order = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value
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
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_image:
            if hasattr(self.item_image, 'to_alipay_dict'):
                params['item_image'] = self.item_image.to_alipay_dict()
            else:
                params['item_image'] = self.item_image
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_order:
            if hasattr(self.item_order, 'to_alipay_dict'):
                params['item_order'] = self.item_order.to_alipay_dict()
            else:
                params['item_order'] = self.item_order
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
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
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSearchboxItemSyncModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_image' in d:
            o.item_image = d['item_image']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_order' in d:
            o.item_order = d['item_order']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'item_url' in d:
            o.item_url = d['item_url']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        return o


