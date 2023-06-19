#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StarUidAmountRatioDTO import StarUidAmountRatioDTO


class RealAmountRatioIncentiveRule(object):

    def __init__(self):
        self._amount_min = None
        self._default_ratio = None
        self._max_amount = None
        self._max_count = None
        self._star_uid_list = None

    @property
    def amount_min(self):
        return self._amount_min

    @amount_min.setter
    def amount_min(self, value):
        self._amount_min = value
    @property
    def default_ratio(self):
        return self._default_ratio

    @default_ratio.setter
    def default_ratio(self, value):
        self._default_ratio = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def star_uid_list(self):
        return self._star_uid_list

    @star_uid_list.setter
    def star_uid_list(self, value):
        if isinstance(value, list):
            self._star_uid_list = list()
            for i in value:
                if isinstance(i, StarUidAmountRatioDTO):
                    self._star_uid_list.append(i)
                else:
                    self._star_uid_list.append(StarUidAmountRatioDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.amount_min:
            if hasattr(self.amount_min, 'to_alipay_dict'):
                params['amount_min'] = self.amount_min.to_alipay_dict()
            else:
                params['amount_min'] = self.amount_min
        if self.default_ratio:
            if hasattr(self.default_ratio, 'to_alipay_dict'):
                params['default_ratio'] = self.default_ratio.to_alipay_dict()
            else:
                params['default_ratio'] = self.default_ratio
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        if self.star_uid_list:
            if isinstance(self.star_uid_list, list):
                for i in range(0, len(self.star_uid_list)):
                    element = self.star_uid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.star_uid_list[i] = element.to_alipay_dict()
            if hasattr(self.star_uid_list, 'to_alipay_dict'):
                params['star_uid_list'] = self.star_uid_list.to_alipay_dict()
            else:
                params['star_uid_list'] = self.star_uid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RealAmountRatioIncentiveRule()
        if 'amount_min' in d:
            o.amount_min = d['amount_min']
        if 'default_ratio' in d:
            o.default_ratio = d['default_ratio']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'max_count' in d:
            o.max_count = d['max_count']
        if 'star_uid_list' in d:
            o.star_uid_list = d['star_uid_list']
        return o


