#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundHistory(object):

    def __init__(self):
        self._amount = None
        self._create_time = None
        self._fund_order_no = None
        self._pay_time = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def fund_order_no(self):
        return self._fund_order_no

    @fund_order_no.setter
    def fund_order_no(self, value):
        self._fund_order_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.fund_order_no:
            if hasattr(self.fund_order_no, 'to_alipay_dict'):
                params['fund_order_no'] = self.fund_order_no.to_alipay_dict()
            else:
                params['fund_order_no'] = self.fund_order_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundHistory()
        if 'amount' in d:
            o.amount = d['amount']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'fund_order_no' in d:
            o.fund_order_no = d['fund_order_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'status' in d:
            o.status = d['status']
        return o


