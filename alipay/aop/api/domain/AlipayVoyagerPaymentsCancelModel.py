#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayVoyagerPaymentsCancelModel(object):

    def __init__(self):
        self._open_id = None
        self._pay_order_id = None
        self._payment_request_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def payment_request_id(self):
        return self._payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self._payment_request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.payment_request_id:
            if hasattr(self.payment_request_id, 'to_alipay_dict'):
                params['payment_request_id'] = self.payment_request_id.to_alipay_dict()
            else:
                params['payment_request_id'] = self.payment_request_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayVoyagerPaymentsCancelModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'payment_request_id' in d:
            o.payment_request_id = d['payment_request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


