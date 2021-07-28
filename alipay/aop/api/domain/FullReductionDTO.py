#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FullReductionDTO(object):

    def __init__(self):
        self._full_reduction_only = None
        self._full_reduction_sku_id = None
        self._min_consumption = None
        self._min_nums = None
        self._promotion_sku_id = None
        self._reduction_amount = None

    @property
    def full_reduction_only(self):
        return self._full_reduction_only

    @full_reduction_only.setter
    def full_reduction_only(self, value):
        self._full_reduction_only = value
    @property
    def full_reduction_sku_id(self):
        return self._full_reduction_sku_id

    @full_reduction_sku_id.setter
    def full_reduction_sku_id(self, value):
        if isinstance(value, list):
            self._full_reduction_sku_id = list()
            for i in value:
                self._full_reduction_sku_id.append(i)
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
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.full_reduction_only:
            if hasattr(self.full_reduction_only, 'to_alipay_dict'):
                params['full_reduction_only'] = self.full_reduction_only.to_alipay_dict()
            else:
                params['full_reduction_only'] = self.full_reduction_only
        if self.full_reduction_sku_id:
            if isinstance(self.full_reduction_sku_id, list):
                for i in range(0, len(self.full_reduction_sku_id)):
                    element = self.full_reduction_sku_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.full_reduction_sku_id[i] = element.to_alipay_dict()
            if hasattr(self.full_reduction_sku_id, 'to_alipay_dict'):
                params['full_reduction_sku_id'] = self.full_reduction_sku_id.to_alipay_dict()
            else:
                params['full_reduction_sku_id'] = self.full_reduction_sku_id
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
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FullReductionDTO()
        if 'full_reduction_only' in d:
            o.full_reduction_only = d['full_reduction_only']
        if 'full_reduction_sku_id' in d:
            o.full_reduction_sku_id = d['full_reduction_sku_id']
        if 'min_consumption' in d:
            o.min_consumption = d['min_consumption']
        if 'min_nums' in d:
            o.min_nums = d['min_nums']
        if 'promotion_sku_id' in d:
            o.promotion_sku_id = d['promotion_sku_id']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        return o


