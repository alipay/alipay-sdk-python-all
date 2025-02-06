#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountLogListDTO(object):

    def __init__(self):
        self._action_type = None
        self._balance = None
        self._currency = None
        self._out_biz_no = None
        self._trans_amount = None
        self._trans_time = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_time(self):
        return self._trans_time

    @trans_time.setter
    def trans_time(self, value):
        self._trans_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_time:
            if hasattr(self.trans_time, 'to_alipay_dict'):
                params['trans_time'] = self.trans_time.to_alipay_dict()
            else:
                params['trans_time'] = self.trans_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountLogListDTO()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'balance' in d:
            o.balance = d['balance']
        if 'currency' in d:
            o.currency = d['currency']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_time' in d:
            o.trans_time = d['trans_time']
        return o


