#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTradeSyncModel(object):

    def __init__(self):
        self._edu_trade_no = None
        self._out_order_no = None
        self._pay_amount = None
        self._pay_time = None
        self._trade_no = None
        self._trade_status = None

    @property
    def edu_trade_no(self):
        return self._edu_trade_no

    @edu_trade_no.setter
    def edu_trade_no(self, value):
        self._edu_trade_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.edu_trade_no:
            if hasattr(self.edu_trade_no, 'to_alipay_dict'):
                params['edu_trade_no'] = self.edu_trade_no.to_alipay_dict()
            else:
                params['edu_trade_no'] = self.edu_trade_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTradeSyncModel()
        if 'edu_trade_no' in d:
            o.edu_trade_no = d['edu_trade_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        return o


