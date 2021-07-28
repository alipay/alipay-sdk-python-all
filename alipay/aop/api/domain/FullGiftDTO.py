#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FullGiftDTO(object):

    def __init__(self):
        self._gift_amount = None
        self._gift_min_consumption = None
        self._gift_nums = None
        self._gift_sku_id = None
        self._min_consumption = None
        self._min_nums = None
        self._promotion_sku_id = None

    @property
    def gift_amount(self):
        return self._gift_amount

    @gift_amount.setter
    def gift_amount(self, value):
        self._gift_amount = value
    @property
    def gift_min_consumption(self):
        return self._gift_min_consumption

    @gift_min_consumption.setter
    def gift_min_consumption(self, value):
        self._gift_min_consumption = value
    @property
    def gift_nums(self):
        return self._gift_nums

    @gift_nums.setter
    def gift_nums(self, value):
        self._gift_nums = value
    @property
    def gift_sku_id(self):
        return self._gift_sku_id

    @gift_sku_id.setter
    def gift_sku_id(self, value):
        if isinstance(value, list):
            self._gift_sku_id = list()
            for i in value:
                self._gift_sku_id.append(i)
    @property
    def min_consumption(self):
        return self._min_consumption

    @min_consumption.setter
    def min_consumption(self, value):
        self._min_consumption = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.gift_amount:
            if hasattr(self.gift_amount, 'to_alipay_dict'):
                params['gift_amount'] = self.gift_amount.to_alipay_dict()
            else:
                params['gift_amount'] = self.gift_amount
        if self.gift_min_consumption:
            if hasattr(self.gift_min_consumption, 'to_alipay_dict'):
                params['gift_min_consumption'] = self.gift_min_consumption.to_alipay_dict()
            else:
                params['gift_min_consumption'] = self.gift_min_consumption
        if self.gift_nums:
            if hasattr(self.gift_nums, 'to_alipay_dict'):
                params['gift_nums'] = self.gift_nums.to_alipay_dict()
            else:
                params['gift_nums'] = self.gift_nums
        if self.gift_sku_id:
            if isinstance(self.gift_sku_id, list):
                for i in range(0, len(self.gift_sku_id)):
                    element = self.gift_sku_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gift_sku_id[i] = element.to_alipay_dict()
            if hasattr(self.gift_sku_id, 'to_alipay_dict'):
                params['gift_sku_id'] = self.gift_sku_id.to_alipay_dict()
            else:
                params['gift_sku_id'] = self.gift_sku_id
        if self.min_consumption:
            if hasattr(self.min_consumption, 'to_alipay_dict'):
                params['min_consumption'] = self.min_consumption.to_alipay_dict()
            else:
                params['min_consumption'] = self.min_consumption
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FullGiftDTO()
        if 'gift_amount' in d:
            o.gift_amount = d['gift_amount']
        if 'gift_min_consumption' in d:
            o.gift_min_consumption = d['gift_min_consumption']
        if 'gift_nums' in d:
            o.gift_nums = d['gift_nums']
        if 'gift_sku_id' in d:
            o.gift_sku_id = d['gift_sku_id']
        if 'min_consumption' in d:
            o.min_consumption = d['min_consumption']
        if 'min_nums' in d:
            o.min_nums = d['min_nums']
        if 'promotion_sku_id' in d:
            o.promotion_sku_id = d['promotion_sku_id']
        return o


