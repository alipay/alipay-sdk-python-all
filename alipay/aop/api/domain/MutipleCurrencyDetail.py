#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MutipleCurrencyDetail(object):

    def __init__(self):
        self._ext_info = None
        self._payment_amount = None
        self._payment_currency = None
        self._settlement_amount = None
        self._settlement_currency = None
        self._trans_amount = None
        self._trans_currency = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_currency(self):
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self._payment_currency = value
    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def settlement_currency(self):
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self._settlement_currency = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_currency:
            if hasattr(self.payment_currency, 'to_alipay_dict'):
                params['payment_currency'] = self.payment_currency.to_alipay_dict()
            else:
                params['payment_currency'] = self.payment_currency
        if self.settlement_amount:
            if hasattr(self.settlement_amount, 'to_alipay_dict'):
                params['settlement_amount'] = self.settlement_amount.to_alipay_dict()
            else:
                params['settlement_amount'] = self.settlement_amount
        if self.settlement_currency:
            if hasattr(self.settlement_currency, 'to_alipay_dict'):
                params['settlement_currency'] = self.settlement_currency.to_alipay_dict()
            else:
                params['settlement_currency'] = self.settlement_currency
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MutipleCurrencyDetail()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_currency' in d:
            o.payment_currency = d['payment_currency']
        if 'settlement_amount' in d:
            o.settlement_amount = d['settlement_amount']
        if 'settlement_currency' in d:
            o.settlement_currency = d['settlement_currency']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        return o


