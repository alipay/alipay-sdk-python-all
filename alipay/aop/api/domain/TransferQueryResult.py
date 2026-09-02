#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferQueryResult(object):

    def __init__(self):
        self._pay_order_trade_no = None
        self._trade_no = None
        self._transfer_pay_results = None

    @property
    def pay_order_trade_no(self):
        return self._pay_order_trade_no

    @pay_order_trade_no.setter
    def pay_order_trade_no(self, value):
        self._pay_order_trade_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def transfer_pay_results(self):
        return self._transfer_pay_results

    @transfer_pay_results.setter
    def transfer_pay_results(self, value):
        self._transfer_pay_results = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_order_trade_no:
            if hasattr(self.pay_order_trade_no, 'to_alipay_dict'):
                params['pay_order_trade_no'] = self.pay_order_trade_no.to_alipay_dict()
            else:
                params['pay_order_trade_no'] = self.pay_order_trade_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.transfer_pay_results:
            if hasattr(self.transfer_pay_results, 'to_alipay_dict'):
                params['transfer_pay_results'] = self.transfer_pay_results.to_alipay_dict()
            else:
                params['transfer_pay_results'] = self.transfer_pay_results
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferQueryResult()
        if 'pay_order_trade_no' in d:
            o.pay_order_trade_no = d['pay_order_trade_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'transfer_pay_results' in d:
            o.transfer_pay_results = d['transfer_pay_results']
        return o


