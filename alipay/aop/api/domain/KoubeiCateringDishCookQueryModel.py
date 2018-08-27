#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishCookQueryModel(object):

    def __init__(self):
        self._cook_id = None
        self._cook_status = None
        self._detail_catetory_big_id = None
        self._detail_catetory_small_id = None
        self._detail_status = None
        self._dish_id = None
        self._merchant_id = None

    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def cook_status(self):
        return self._cook_status

    @cook_status.setter
    def cook_status(self, value):
        self._cook_status = value
    @property
    def detail_catetory_big_id(self):
        return self._detail_catetory_big_id

    @detail_catetory_big_id.setter
    def detail_catetory_big_id(self, value):
        self._detail_catetory_big_id = value
    @property
    def detail_catetory_small_id(self):
        return self._detail_catetory_small_id

    @detail_catetory_small_id.setter
    def detail_catetory_small_id(self, value):
        self._detail_catetory_small_id = value
    @property
    def detail_status(self):
        return self._detail_status

    @detail_status.setter
    def detail_status(self, value):
        self._detail_status = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.cook_status:
            if hasattr(self.cook_status, 'to_alipay_dict'):
                params['cook_status'] = self.cook_status.to_alipay_dict()
            else:
                params['cook_status'] = self.cook_status
        if self.detail_catetory_big_id:
            if hasattr(self.detail_catetory_big_id, 'to_alipay_dict'):
                params['detail_catetory_big_id'] = self.detail_catetory_big_id.to_alipay_dict()
            else:
                params['detail_catetory_big_id'] = self.detail_catetory_big_id
        if self.detail_catetory_small_id:
            if hasattr(self.detail_catetory_small_id, 'to_alipay_dict'):
                params['detail_catetory_small_id'] = self.detail_catetory_small_id.to_alipay_dict()
            else:
                params['detail_catetory_small_id'] = self.detail_catetory_small_id
        if self.detail_status:
            if hasattr(self.detail_status, 'to_alipay_dict'):
                params['detail_status'] = self.detail_status.to_alipay_dict()
            else:
                params['detail_status'] = self.detail_status
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCookQueryModel()
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'cook_status' in d:
            o.cook_status = d['cook_status']
        if 'detail_catetory_big_id' in d:
            o.detail_catetory_big_id = d['detail_catetory_big_id']
        if 'detail_catetory_small_id' in d:
            o.detail_catetory_small_id = d['detail_catetory_small_id']
        if 'detail_status' in d:
            o.detail_status = d['detail_status']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


