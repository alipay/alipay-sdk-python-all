#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RechargeDTO(object):

    def __init__(self):
        self._gift_amount = None
        self._gift_nums = None
        self._gift_sku_id = None
        self._recharge_amount = None

    @property
    def gift_amount(self):
        return self._gift_amount

    @gift_amount.setter
    def gift_amount(self, value):
        self._gift_amount = value
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
    def recharge_amount(self):
        return self._recharge_amount

    @recharge_amount.setter
    def recharge_amount(self, value):
        self._recharge_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.gift_amount:
            if hasattr(self.gift_amount, 'to_alipay_dict'):
                params['gift_amount'] = self.gift_amount.to_alipay_dict()
            else:
                params['gift_amount'] = self.gift_amount
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
        if self.recharge_amount:
            if hasattr(self.recharge_amount, 'to_alipay_dict'):
                params['recharge_amount'] = self.recharge_amount.to_alipay_dict()
            else:
                params['recharge_amount'] = self.recharge_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RechargeDTO()
        if 'gift_amount' in d:
            o.gift_amount = d['gift_amount']
        if 'gift_nums' in d:
            o.gift_nums = d['gift_nums']
        if 'gift_sku_id' in d:
            o.gift_sku_id = d['gift_sku_id']
        if 'recharge_amount' in d:
            o.recharge_amount = d['recharge_amount']
        return o


