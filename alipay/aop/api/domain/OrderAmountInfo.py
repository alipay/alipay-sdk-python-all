#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderAmountInfo(object):

    def __init__(self):
        self._amount_discount = None
        self._amount_item = None
        self._amount_original = None
        self._discount_total = None
        self._nurse_visit_fee = None

    @property
    def amount_discount(self):
        return self._amount_discount

    @amount_discount.setter
    def amount_discount(self, value):
        self._amount_discount = value
    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def amount_original(self):
        return self._amount_original

    @amount_original.setter
    def amount_original(self, value):
        self._amount_original = value
    @property
    def discount_total(self):
        return self._discount_total

    @discount_total.setter
    def discount_total(self, value):
        self._discount_total = value
    @property
    def nurse_visit_fee(self):
        return self._nurse_visit_fee

    @nurse_visit_fee.setter
    def nurse_visit_fee(self, value):
        self._nurse_visit_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_discount:
            if hasattr(self.amount_discount, 'to_alipay_dict'):
                params['amount_discount'] = self.amount_discount.to_alipay_dict()
            else:
                params['amount_discount'] = self.amount_discount
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.amount_original:
            if hasattr(self.amount_original, 'to_alipay_dict'):
                params['amount_original'] = self.amount_original.to_alipay_dict()
            else:
                params['amount_original'] = self.amount_original
        if self.discount_total:
            if hasattr(self.discount_total, 'to_alipay_dict'):
                params['discount_total'] = self.discount_total.to_alipay_dict()
            else:
                params['discount_total'] = self.discount_total
        if self.nurse_visit_fee:
            if hasattr(self.nurse_visit_fee, 'to_alipay_dict'):
                params['nurse_visit_fee'] = self.nurse_visit_fee.to_alipay_dict()
            else:
                params['nurse_visit_fee'] = self.nurse_visit_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderAmountInfo()
        if 'amount_discount' in d:
            o.amount_discount = d['amount_discount']
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'amount_original' in d:
            o.amount_original = d['amount_original']
        if 'discount_total' in d:
            o.discount_total = d['discount_total']
        if 'nurse_visit_fee' in d:
            o.nurse_visit_fee = d['nurse_visit_fee']
        return o


