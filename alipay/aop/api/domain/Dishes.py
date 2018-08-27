#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Dishes(object):

    def __init__(self):
        self._dish_id = None
        self._dish_name = None
        self._dish_num = None
        self._dish_price = None
        self._dish_real_price = None
        self._dish_skuid = None

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
    def dish_num(self):
        return self._dish_num

    @dish_num.setter
    def dish_num(self, value):
        self._dish_num = value
    @property
    def dish_price(self):
        return self._dish_price

    @dish_price.setter
    def dish_price(self, value):
        self._dish_price = value
    @property
    def dish_real_price(self):
        return self._dish_real_price

    @dish_real_price.setter
    def dish_real_price(self, value):
        self._dish_real_price = value
    @property
    def dish_skuid(self):
        return self._dish_skuid

    @dish_skuid.setter
    def dish_skuid(self, value):
        self._dish_skuid = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.dish_num:
            if hasattr(self.dish_num, 'to_alipay_dict'):
                params['dish_num'] = self.dish_num.to_alipay_dict()
            else:
                params['dish_num'] = self.dish_num
        if self.dish_price:
            if hasattr(self.dish_price, 'to_alipay_dict'):
                params['dish_price'] = self.dish_price.to_alipay_dict()
            else:
                params['dish_price'] = self.dish_price
        if self.dish_real_price:
            if hasattr(self.dish_real_price, 'to_alipay_dict'):
                params['dish_real_price'] = self.dish_real_price.to_alipay_dict()
            else:
                params['dish_real_price'] = self.dish_real_price
        if self.dish_skuid:
            if hasattr(self.dish_skuid, 'to_alipay_dict'):
                params['dish_skuid'] = self.dish_skuid.to_alipay_dict()
            else:
                params['dish_skuid'] = self.dish_skuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Dishes()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_num' in d:
            o.dish_num = d['dish_num']
        if 'dish_price' in d:
            o.dish_price = d['dish_price']
        if 'dish_real_price' in d:
            o.dish_real_price = d['dish_real_price']
        if 'dish_skuid' in d:
            o.dish_skuid = d['dish_skuid']
        return o


