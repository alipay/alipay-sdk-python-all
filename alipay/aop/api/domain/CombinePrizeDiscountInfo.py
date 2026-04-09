#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubPrizeDiscountInfo import SubPrizeDiscountInfo


class CombinePrizeDiscountInfo(object):

    def __init__(self):
        self._allow_voucher_split = None
        self._discount_type = None
        self._sub_prize_list = None
        self._total_amount = None

    @property
    def allow_voucher_split(self):
        return self._allow_voucher_split

    @allow_voucher_split.setter
    def allow_voucher_split(self, value):
        self._allow_voucher_split = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def sub_prize_list(self):
        return self._sub_prize_list

    @sub_prize_list.setter
    def sub_prize_list(self, value):
        if isinstance(value, list):
            self._sub_prize_list = list()
            for i in value:
                if isinstance(i, SubPrizeDiscountInfo):
                    self._sub_prize_list.append(i)
                else:
                    self._sub_prize_list.append(SubPrizeDiscountInfo.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_voucher_split:
            if hasattr(self.allow_voucher_split, 'to_alipay_dict'):
                params['allow_voucher_split'] = self.allow_voucher_split.to_alipay_dict()
            else:
                params['allow_voucher_split'] = self.allow_voucher_split
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.sub_prize_list:
            if isinstance(self.sub_prize_list, list):
                for i in range(0, len(self.sub_prize_list)):
                    element = self.sub_prize_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_prize_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_prize_list, 'to_alipay_dict'):
                params['sub_prize_list'] = self.sub_prize_list.to_alipay_dict()
            else:
                params['sub_prize_list'] = self.sub_prize_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CombinePrizeDiscountInfo()
        if 'allow_voucher_split' in d:
            o.allow_voucher_split = d['allow_voucher_split']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'sub_prize_list' in d:
            o.sub_prize_list = d['sub_prize_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


