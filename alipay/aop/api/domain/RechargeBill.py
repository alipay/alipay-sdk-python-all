#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RechargeBill(object):

    def __init__(self):
        self._amount = None
        self._deposit_time = None
        self._status = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def deposit_time(self):
        return self._deposit_time

    @deposit_time.setter
    def deposit_time(self, value):
        self._deposit_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.deposit_time:
            if hasattr(self.deposit_time, 'to_alipay_dict'):
                params['deposit_time'] = self.deposit_time.to_alipay_dict()
            else:
                params['deposit_time'] = self.deposit_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RechargeBill()
        if 'amount' in d:
            o.amount = d['amount']
        if 'deposit_time' in d:
            o.deposit_time = d['deposit_time']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


