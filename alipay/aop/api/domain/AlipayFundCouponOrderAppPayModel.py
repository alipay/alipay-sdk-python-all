#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponOrderAppPayModel(object):

    def __init__(self):
        self._amount = None
        self._extra_param = None
        self._order_title = None
        self._out_order_no = None
        self._out_request_no = None
        self._pay_timeout = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_timeout(self):
        return self._pay_timeout

    @pay_timeout.setter
    def pay_timeout(self, value):
        self._pay_timeout = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_timeout:
            if hasattr(self.pay_timeout, 'to_alipay_dict'):
                params['pay_timeout'] = self.pay_timeout.to_alipay_dict()
            else:
                params['pay_timeout'] = self.pay_timeout
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundCouponOrderAppPayModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_timeout' in d:
            o.pay_timeout = d['pay_timeout']
        return o


