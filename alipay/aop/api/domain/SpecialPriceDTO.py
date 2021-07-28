#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecialPriceDTO(object):

    def __init__(self):
        self._min_nums = None
        self._promotion_sku_id = None
        self._special_price = None
        self._special_price_only = None
        self._special_price_sku_id = None

    @property
    def min_nums(self):
        return self._min_nums

    @min_nums.setter
    def min_nums(self, value):
        self._min_nums = value
    @property
    def promotion_sku_id(self):
        return self._promotion_sku_id

    @promotion_sku_id.setter
    def promotion_sku_id(self, value):
        if isinstance(value, list):
            self._promotion_sku_id = list()
            for i in value:
                self._promotion_sku_id.append(i)
    @property
    def special_price(self):
        return self._special_price

    @special_price.setter
    def special_price(self, value):
        self._special_price = value
    @property
    def special_price_only(self):
        return self._special_price_only

    @special_price_only.setter
    def special_price_only(self, value):
        self._special_price_only = value
    @property
    def special_price_sku_id(self):
        return self._special_price_sku_id

    @special_price_sku_id.setter
    def special_price_sku_id(self, value):
        if isinstance(value, list):
            self._special_price_sku_id = list()
            for i in value:
                self._special_price_sku_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.min_nums:
            if hasattr(self.min_nums, 'to_alipay_dict'):
                params['min_nums'] = self.min_nums.to_alipay_dict()
            else:
                params['min_nums'] = self.min_nums
        if self.promotion_sku_id:
            if isinstance(self.promotion_sku_id, list):
                for i in range(0, len(self.promotion_sku_id)):
                    element = self.promotion_sku_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promotion_sku_id[i] = element.to_alipay_dict()
            if hasattr(self.promotion_sku_id, 'to_alipay_dict'):
                params['promotion_sku_id'] = self.promotion_sku_id.to_alipay_dict()
            else:
                params['promotion_sku_id'] = self.promotion_sku_id
        if self.special_price:
            if hasattr(self.special_price, 'to_alipay_dict'):
                params['special_price'] = self.special_price.to_alipay_dict()
            else:
                params['special_price'] = self.special_price
        if self.special_price_only:
            if hasattr(self.special_price_only, 'to_alipay_dict'):
                params['special_price_only'] = self.special_price_only.to_alipay_dict()
            else:
                params['special_price_only'] = self.special_price_only
        if self.special_price_sku_id:
            if isinstance(self.special_price_sku_id, list):
                for i in range(0, len(self.special_price_sku_id)):
                    element = self.special_price_sku_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_price_sku_id[i] = element.to_alipay_dict()
            if hasattr(self.special_price_sku_id, 'to_alipay_dict'):
                params['special_price_sku_id'] = self.special_price_sku_id.to_alipay_dict()
            else:
                params['special_price_sku_id'] = self.special_price_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialPriceDTO()
        if 'min_nums' in d:
            o.min_nums = d['min_nums']
        if 'promotion_sku_id' in d:
            o.promotion_sku_id = d['promotion_sku_id']
        if 'special_price' in d:
            o.special_price = d['special_price']
        if 'special_price_only' in d:
            o.special_price_only = d['special_price_only']
        if 'special_price_sku_id' in d:
            o.special_price_sku_id = d['special_price_sku_id']
        return o


