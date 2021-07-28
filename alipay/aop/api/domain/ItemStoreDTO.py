#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemStoreDTO(object):

    def __init__(self):
        self._brand_name = None
        self._category_name = None
        self._store_address = None
        self._store_id = None
        self._store_logo = None
        self._store_name = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_logo(self):
        return self._store_logo

    @store_logo.setter
    def store_logo(self, value):
        self._store_logo = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_logo:
            if hasattr(self.store_logo, 'to_alipay_dict'):
                params['store_logo'] = self.store_logo.to_alipay_dict()
            else:
                params['store_logo'] = self.store_logo
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemStoreDTO()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_logo' in d:
            o.store_logo = d['store_logo']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


