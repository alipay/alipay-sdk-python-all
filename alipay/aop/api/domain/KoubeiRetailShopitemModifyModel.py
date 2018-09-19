#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailShopitemModifyModel(object):

    def __init__(self):
        self._brand_code = None
        self._category_code = None
        self._description = None
        self._item_code = None
        self._kb_shop_id = None
        self._price = None
        self._title = None

    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def kb_shop_id(self):
        return self._kb_shop_id

    @kb_shop_id.setter
    def kb_shop_id(self, value):
        self._kb_shop_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.kb_shop_id:
            if hasattr(self.kb_shop_id, 'to_alipay_dict'):
                params['kb_shop_id'] = self.kb_shop_id.to_alipay_dict()
            else:
                params['kb_shop_id'] = self.kb_shop_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailShopitemModifyModel()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'description' in d:
            o.description = d['description']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'kb_shop_id' in d:
            o.kb_shop_id = d['kb_shop_id']
        if 'price' in d:
            o.price = d['price']
        if 'title' in d:
            o.title = d['title']
        return o


