#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionRefundOrderInfo(object):

    def __init__(self):
        self._biz_time = None
        self._refund_amount = None
        self._refund_cash = None
        self._refund_order_id = None
        self._refund_status = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.refund_order_id:
            if hasattr(self.refund_order_id, 'to_alipay_dict'):
                params['refund_order_id'] = self.refund_order_id.to_alipay_dict()
            else:
                params['refund_order_id'] = self.refund_order_id
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionRefundOrderInfo()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'refund_order_id' in d:
            o.refund_order_id = d['refund_order_id']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        return o


