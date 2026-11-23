#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderParams(object):

    def __init__(self):
        self._biz_order_no = None
        self._merchant_pid = None
        self._order_amount = None

    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderParams()
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        return o


