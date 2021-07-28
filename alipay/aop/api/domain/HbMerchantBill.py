#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbMerchantBill(object):

    def __init__(self):
        self._discount_amount = None
        self._out_order_no = None
        self._period_num = None
        self._trade_amount = None
        self._trade_no = None
        self._trade_time = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbMerchantBill()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


