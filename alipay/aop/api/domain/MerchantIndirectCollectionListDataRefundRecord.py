#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantIndirectCollectionListDataRefundRecord(object):

    def __init__(self):
        self._amount = None
        self._origin_order_no = None
        self._pay_channel = None
        self._refund_status = None
        self._trade_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def origin_order_no(self):
        return self._origin_order_no

    @origin_order_no.setter
    def origin_order_no(self, value):
        self._origin_order_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.origin_order_no:
            if hasattr(self.origin_order_no, 'to_alipay_dict'):
                params['origin_order_no'] = self.origin_order_no.to_alipay_dict()
            else:
                params['origin_order_no'] = self.origin_order_no
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
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
        o = MerchantIndirectCollectionListDataRefundRecord()
        if 'amount' in d:
            o.amount = d['amount']
        if 'origin_order_no' in d:
            o.origin_order_no = d['origin_order_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


