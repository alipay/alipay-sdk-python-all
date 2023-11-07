#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LivestreamOrder(object):

    def __init__(self):
        self._order_amount = None
        self._order_id = None
        self._payment_time = None
        self._receipt_confirm_time = None
        self._streamer_id = None

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def receipt_confirm_time(self):
        return self._receipt_confirm_time

    @receipt_confirm_time.setter
    def receipt_confirm_time(self, value):
        self._receipt_confirm_time = value
    @property
    def streamer_id(self):
        return self._streamer_id

    @streamer_id.setter
    def streamer_id(self, value):
        self._streamer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.receipt_confirm_time:
            if hasattr(self.receipt_confirm_time, 'to_alipay_dict'):
                params['receipt_confirm_time'] = self.receipt_confirm_time.to_alipay_dict()
            else:
                params['receipt_confirm_time'] = self.receipt_confirm_time
        if self.streamer_id:
            if hasattr(self.streamer_id, 'to_alipay_dict'):
                params['streamer_id'] = self.streamer_id.to_alipay_dict()
            else:
                params['streamer_id'] = self.streamer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LivestreamOrder()
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'receipt_confirm_time' in d:
            o.receipt_confirm_time = d['receipt_confirm_time']
        if 'streamer_id' in d:
            o.streamer_id = d['streamer_id']
        return o


