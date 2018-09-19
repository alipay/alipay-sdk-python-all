#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankFinanceYulibaoCapitalRansomModel(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._fund_code = None
        self._out_biz_no = None
        self._ransom_mode = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def ransom_mode(self):
        return self._ransom_mode

    @ransom_mode.setter
    def ransom_mode(self, value):
        self._ransom_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.fund_code:
            if hasattr(self.fund_code, 'to_alipay_dict'):
                params['fund_code'] = self.fund_code.to_alipay_dict()
            else:
                params['fund_code'] = self.fund_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.ransom_mode:
            if hasattr(self.ransom_mode, 'to_alipay_dict'):
                params['ransom_mode'] = self.ransom_mode.to_alipay_dict()
            else:
                params['ransom_mode'] = self.ransom_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankFinanceYulibaoCapitalRansomModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'fund_code' in d:
            o.fund_code = d['fund_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'ransom_mode' in d:
            o.ransom_mode = d['ransom_mode']
        return o


