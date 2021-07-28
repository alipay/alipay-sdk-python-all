#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetFundInfo(object):

    def __init__(self):
        self._amount = None
        self._fund_account = None
        self._fund_type = None
        self._settle_dead_line = None
        self._settle_mode = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def settle_dead_line(self):
        return self._settle_dead_line

    @settle_dead_line.setter
    def settle_dead_line(self, value):
        self._settle_dead_line = value
    @property
    def settle_mode(self):
        return self._settle_mode

    @settle_mode.setter
    def settle_mode(self, value):
        self._settle_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_account:
            if hasattr(self.fund_account, 'to_alipay_dict'):
                params['fund_account'] = self.fund_account.to_alipay_dict()
            else:
                params['fund_account'] = self.fund_account
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.settle_dead_line:
            if hasattr(self.settle_dead_line, 'to_alipay_dict'):
                params['settle_dead_line'] = self.settle_dead_line.to_alipay_dict()
            else:
                params['settle_dead_line'] = self.settle_dead_line
        if self.settle_mode:
            if hasattr(self.settle_mode, 'to_alipay_dict'):
                params['settle_mode'] = self.settle_mode.to_alipay_dict()
            else:
                params['settle_mode'] = self.settle_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetFundInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_account' in d:
            o.fund_account = d['fund_account']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'settle_dead_line' in d:
            o.settle_dead_line = d['settle_dead_line']
        if 'settle_mode' in d:
            o.settle_mode = d['settle_mode']
        return o


