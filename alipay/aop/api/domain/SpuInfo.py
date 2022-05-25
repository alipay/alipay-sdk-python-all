#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuInfo(object):

    def __init__(self):
        self._brand = None
        self._category = None
        self._count = None
        self._icon = None
        self._price = None
        self._provider = None
        self._spu_id = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, value):
        self._provider = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.provider:
            if hasattr(self.provider, 'to_alipay_dict'):
                params['provider'] = self.provider.to_alipay_dict()
            else:
                params['provider'] = self.provider
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpuInfo()
        if 'brand' in d:
            o.brand = d['brand']
        if 'category' in d:
            o.category = d['category']
        if 'count' in d:
            o.count = d['count']
        if 'icon' in d:
            o.icon = d['icon']
        if 'price' in d:
            o.price = d['price']
        if 'provider' in d:
            o.provider = d['provider']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        return o


