#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemBo import ItemBo
from alipay.aop.api.domain.ItemBo import ItemBo


class TBMiniShopBo(object):

    def __init__(self):
        self._address = None
        self._attribute = None
        self._coupons = None
        self._items = None
        self._logo_url = None
        self._mini_shop_id = None
        self._shop_head_name = None
        self._shop_id = None
        self._shop_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, value):
        if isinstance(value, list):
            self._coupons = list()
            for i in value:
                if isinstance(i, ItemBo):
                    self._coupons.append(i)
                else:
                    self._coupons.append(ItemBo.from_alipay_dict(i))
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ItemBo):
                    self._items.append(i)
                else:
                    self._items.append(ItemBo.from_alipay_dict(i))
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def mini_shop_id(self):
        return self._mini_shop_id

    @mini_shop_id.setter
    def mini_shop_id(self, value):
        self._mini_shop_id = value
    @property
    def shop_head_name(self):
        return self._shop_head_name

    @shop_head_name.setter
    def shop_head_name(self, value):
        self._shop_head_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.coupons:
            if isinstance(self.coupons, list):
                for i in range(0, len(self.coupons)):
                    element = self.coupons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupons[i] = element.to_alipay_dict()
            if hasattr(self.coupons, 'to_alipay_dict'):
                params['coupons'] = self.coupons.to_alipay_dict()
            else:
                params['coupons'] = self.coupons
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.mini_shop_id:
            if hasattr(self.mini_shop_id, 'to_alipay_dict'):
                params['mini_shop_id'] = self.mini_shop_id.to_alipay_dict()
            else:
                params['mini_shop_id'] = self.mini_shop_id
        if self.shop_head_name:
            if hasattr(self.shop_head_name, 'to_alipay_dict'):
                params['shop_head_name'] = self.shop_head_name.to_alipay_dict()
            else:
                params['shop_head_name'] = self.shop_head_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TBMiniShopBo()
        if 'address' in d:
            o.address = d['address']
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'coupons' in d:
            o.coupons = d['coupons']
        if 'items' in d:
            o.items = d['items']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'mini_shop_id' in d:
            o.mini_shop_id = d['mini_shop_id']
        if 'shop_head_name' in d:
            o.shop_head_name = d['shop_head_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


