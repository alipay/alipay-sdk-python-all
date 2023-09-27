#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductOrderDetail(object):

    def __init__(self):
        self._deduct_amount = None
        self._order_no = None
        self._produce_amount = None
        self._total_amount = None

    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def produce_amount(self):
        return self._produce_amount

    @produce_amount.setter
    def produce_amount(self, value):
        self._produce_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.produce_amount:
            if hasattr(self.produce_amount, 'to_alipay_dict'):
                params['produce_amount'] = self.produce_amount.to_alipay_dict()
            else:
                params['produce_amount'] = self.produce_amount
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
        o = DeductOrderDetail()
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'produce_amount' in d:
            o.produce_amount = d['produce_amount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


