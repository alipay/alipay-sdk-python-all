#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishQueryModel(object):

    def __init__(self):
        self._catetory_big_id = None
        self._catetory_small_id = None
        self._dish_cuisine = None
        self._dish_id = None
        self._dish_name = None
        self._dish_status = None
        self._en_remember_code = None
        self._merchant_id = None
        self._nb_remember_code = None
        self._shop_id = None
        self._sku_id = None

    @property
    def catetory_big_id(self):
        return self._catetory_big_id

    @catetory_big_id.setter
    def catetory_big_id(self, value):
        self._catetory_big_id = value
    @property
    def catetory_small_id(self):
        return self._catetory_small_id

    @catetory_small_id.setter
    def catetory_small_id(self, value):
        self._catetory_small_id = value
    @property
    def dish_cuisine(self):
        return self._dish_cuisine

    @dish_cuisine.setter
    def dish_cuisine(self, value):
        self._dish_cuisine = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_status(self):
        return self._dish_status

    @dish_status.setter
    def dish_status(self, value):
        self._dish_status = value
    @property
    def en_remember_code(self):
        return self._en_remember_code

    @en_remember_code.setter
    def en_remember_code(self, value):
        self._en_remember_code = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def nb_remember_code(self):
        return self._nb_remember_code

    @nb_remember_code.setter
    def nb_remember_code(self, value):
        self._nb_remember_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_big_id:
            if hasattr(self.catetory_big_id, 'to_alipay_dict'):
                params['catetory_big_id'] = self.catetory_big_id.to_alipay_dict()
            else:
                params['catetory_big_id'] = self.catetory_big_id
        if self.catetory_small_id:
            if hasattr(self.catetory_small_id, 'to_alipay_dict'):
                params['catetory_small_id'] = self.catetory_small_id.to_alipay_dict()
            else:
                params['catetory_small_id'] = self.catetory_small_id
        if self.dish_cuisine:
            if hasattr(self.dish_cuisine, 'to_alipay_dict'):
                params['dish_cuisine'] = self.dish_cuisine.to_alipay_dict()
            else:
                params['dish_cuisine'] = self.dish_cuisine
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_status:
            if hasattr(self.dish_status, 'to_alipay_dict'):
                params['dish_status'] = self.dish_status.to_alipay_dict()
            else:
                params['dish_status'] = self.dish_status
        if self.en_remember_code:
            if hasattr(self.en_remember_code, 'to_alipay_dict'):
                params['en_remember_code'] = self.en_remember_code.to_alipay_dict()
            else:
                params['en_remember_code'] = self.en_remember_code
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.nb_remember_code:
            if hasattr(self.nb_remember_code, 'to_alipay_dict'):
                params['nb_remember_code'] = self.nb_remember_code.to_alipay_dict()
            else:
                params['nb_remember_code'] = self.nb_remember_code
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishQueryModel()
        if 'catetory_big_id' in d:
            o.catetory_big_id = d['catetory_big_id']
        if 'catetory_small_id' in d:
            o.catetory_small_id = d['catetory_small_id']
        if 'dish_cuisine' in d:
            o.dish_cuisine = d['dish_cuisine']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_status' in d:
            o.dish_status = d['dish_status']
        if 'en_remember_code' in d:
            o.en_remember_code = d['en_remember_code']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'nb_remember_code' in d:
            o.nb_remember_code = d['nb_remember_code']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


