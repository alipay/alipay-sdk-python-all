#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsSupplyDiscountInfo(object):

    def __init__(self):
        self._amount = None
        self._ceiling_amount = None
        self._floor_amount = None
        self._origin_amount = None
        self._special_amount = None
        self._voucher_discount_percent = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def special_amount(self):
        return self._special_amount

    @special_amount.setter
    def special_amount(self, value):
        self._special_amount = value
    @property
    def voucher_discount_percent(self):
        return self._voucher_discount_percent

    @voucher_discount_percent.setter
    def voucher_discount_percent(self, value):
        self._voucher_discount_percent = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.special_amount:
            if hasattr(self.special_amount, 'to_alipay_dict'):
                params['special_amount'] = self.special_amount.to_alipay_dict()
            else:
                params['special_amount'] = self.special_amount
        if self.voucher_discount_percent:
            if hasattr(self.voucher_discount_percent, 'to_alipay_dict'):
                params['voucher_discount_percent'] = self.voucher_discount_percent.to_alipay_dict()
            else:
                params['voucher_discount_percent'] = self.voucher_discount_percent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsSupplyDiscountInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'special_amount' in d:
            o.special_amount = d['special_amount']
        if 'voucher_discount_percent' in d:
            o.voucher_discount_percent = d['voucher_discount_percent']
        return o


