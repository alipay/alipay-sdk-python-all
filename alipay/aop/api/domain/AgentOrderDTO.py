#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentOrderDTO(object):

    def __init__(self):
        self._actual_amount = None
        self._amount = None
        self._discount_amount = None
        self._out_shake_no = None
        self._pay_time = None
        self._seller_name = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def out_shake_no(self):
        return self._out_shake_no

    @out_shake_no.setter
    def out_shake_no(self, value):
        self._out_shake_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.out_shake_no:
            if hasattr(self.out_shake_no, 'to_alipay_dict'):
                params['out_shake_no'] = self.out_shake_no.to_alipay_dict()
            else:
                params['out_shake_no'] = self.out_shake_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentOrderDTO()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'out_shake_no' in d:
            o.out_shake_no = d['out_shake_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        return o


