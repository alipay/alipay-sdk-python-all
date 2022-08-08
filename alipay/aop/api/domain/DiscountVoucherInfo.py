#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountVoucherInfo(object):

    def __init__(self):
        self._ceiling_amount = None
        self._discount = None
        self._floor_amount = None

    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountVoucherInfo()
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'discount' in d:
            o.discount = d['discount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        return o


