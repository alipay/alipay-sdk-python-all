#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundInfo(object):

    def __init__(self):
        self._amount = None
        self._item_order_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def item_order_no(self):
        return self._item_order_no

    @item_order_no.setter
    def item_order_no(self, value):
        self._item_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.item_order_no:
            if hasattr(self.item_order_no, 'to_alipay_dict'):
                params['item_order_no'] = self.item_order_no.to_alipay_dict()
            else:
                params['item_order_no'] = self.item_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'item_order_no' in d:
            o.item_order_no = d['item_order_no']
        return o


