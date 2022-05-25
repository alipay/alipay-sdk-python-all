#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberWalletBalanceDetailVO(object):

    def __init__(self):
        self._benefit_amount = None
        self._principal_amount = None
        self._trade_amount = None
        self._trade_no = None
        self._trade_time = None
        self._trade_type = None

    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def principal_amount(self):
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, value):
        self._principal_amount = value
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
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.principal_amount:
            if hasattr(self.principal_amount, 'to_alipay_dict'):
                params['principal_amount'] = self.principal_amount.to_alipay_dict()
            else:
                params['principal_amount'] = self.principal_amount
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
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberWalletBalanceDetailVO()
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'principal_amount' in d:
            o.principal_amount = d['principal_amount']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


