#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopAppRelation(object):

    def __init__(self):
        self._shop_id = None
        self._store_app_id = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_app_id(self):
        return self._store_app_id

    @store_app_id.setter
    def store_app_id(self, value):
        self._store_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_app_id:
            if hasattr(self.store_app_id, 'to_alipay_dict'):
                params['store_app_id'] = self.store_app_id.to_alipay_dict()
            else:
                params['store_app_id'] = self.store_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopAppRelation()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_app_id' in d:
            o.store_app_id = d['store_app_id']
        return o


