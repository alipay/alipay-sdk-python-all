#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtShopItem(object):

    def __init__(self):
        self._brand_code = None
        self._category_code = None
        self._count = None
        self._country = None
        self._description = None
        self._ext_goods_info = None
        self._id = None
        self._item_code = None
        self._kb_shop_id = None
        self._picture = None
        self._price = None
        self._specification = None
        self._system_provider_id = None
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
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_goods_info(self):
        return self._ext_goods_info

    @ext_goods_info.setter
    def ext_goods_info(self, value):
        self._ext_goods_info = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def system_provider_id(self):
        return self._system_provider_id

    @system_provider_id.setter
    def system_provider_id(self, value):
        self._system_provider_id = value
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
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext_goods_info:
            if hasattr(self.ext_goods_info, 'to_alipay_dict'):
                params['ext_goods_info'] = self.ext_goods_info.to_alipay_dict()
            else:
                params['ext_goods_info'] = self.ext_goods_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.system_provider_id:
            if hasattr(self.system_provider_id, 'to_alipay_dict'):
                params['system_provider_id'] = self.system_provider_id.to_alipay_dict()
            else:
                params['system_provider_id'] = self.system_provider_id
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
        o = ExtShopItem()
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'count' in d:
            o.count = d['count']
        if 'country' in d:
            o.country = d['country']
        if 'description' in d:
            o.description = d['description']
        if 'ext_goods_info' in d:
            o.ext_goods_info = d['ext_goods_info']
        if 'id' in d:
            o.id = d['id']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'kb_shop_id' in d:
            o.kb_shop_id = d['kb_shop_id']
        if 'picture' in d:
            o.picture = d['picture']
        if 'price' in d:
            o.price = d['price']
        if 'specification' in d:
            o.specification = d['specification']
        if 'system_provider_id' in d:
            o.system_provider_id = d['system_provider_id']
        if 'title' in d:
            o.title = d['title']
        return o


