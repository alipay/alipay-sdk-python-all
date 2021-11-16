#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityExchangeVoucher(object):

    def __init__(self):
        self._amount = None
        self._floor_amount = None
        self._overdue_refundable = None
        self._refundable = None
        self._sale_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def overdue_refundable(self):
        return self._overdue_refundable

    @overdue_refundable.setter
    def overdue_refundable(self, value):
        self._overdue_refundable = value
    @property
    def refundable(self):
        return self._refundable

    @refundable.setter
    def refundable(self, value):
        self._refundable = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.overdue_refundable:
            if hasattr(self.overdue_refundable, 'to_alipay_dict'):
                params['overdue_refundable'] = self.overdue_refundable.to_alipay_dict()
            else:
                params['overdue_refundable'] = self.overdue_refundable
        if self.refundable:
            if hasattr(self.refundable, 'to_alipay_dict'):
                params['refundable'] = self.refundable.to_alipay_dict()
            else:
                params['refundable'] = self.refundable
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityExchangeVoucher()
        if 'amount' in d:
            o.amount = d['amount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'overdue_refundable' in d:
            o.overdue_refundable = d['overdue_refundable']
        if 'refundable' in d:
            o.refundable = d['refundable']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        return o


