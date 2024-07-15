#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleFundsInfo(object):

    def __init__(self):
        self._fund_serial_no = None
        self._funds_type = None
        self._trade_amount = None
        self._trade_no = None
        self._trade_time = None

    @property
    def fund_serial_no(self):
        return self._fund_serial_no

    @fund_serial_no.setter
    def fund_serial_no(self, value):
        self._fund_serial_no = value
    @property
    def funds_type(self):
        return self._funds_type

    @funds_type.setter
    def funds_type(self, value):
        self._funds_type = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_serial_no:
            if hasattr(self.fund_serial_no, 'to_alipay_dict'):
                params['fund_serial_no'] = self.fund_serial_no.to_alipay_dict()
            else:
                params['fund_serial_no'] = self.fund_serial_no
        if self.funds_type:
            if hasattr(self.funds_type, 'to_alipay_dict'):
                params['funds_type'] = self.funds_type.to_alipay_dict()
            else:
                params['funds_type'] = self.funds_type
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = RecycleFundsInfo()
        if 'fund_serial_no' in d:
            o.fund_serial_no = d['fund_serial_no']
        if 'funds_type' in d:
            o.funds_type = d['funds_type']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


