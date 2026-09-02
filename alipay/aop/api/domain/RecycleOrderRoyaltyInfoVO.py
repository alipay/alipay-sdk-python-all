#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleOrderRoyaltyInfoVO(object):

    def __init__(self):
        self._trade_amount = None
        self._trade_in = None
        self._trade_no = None
        self._trade_status = None
        self._trade_time = None

    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_in(self):
        return self._trade_in

    @trade_in.setter
    def trade_in(self, value):
        self._trade_in = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_in:
            if hasattr(self.trade_in, 'to_alipay_dict'):
                params['trade_in'] = self.trade_in.to_alipay_dict()
            else:
                params['trade_in'] = self.trade_in
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
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
        o = RecycleOrderRoyaltyInfoVO()
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_in' in d:
            o.trade_in = d['trade_in']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


