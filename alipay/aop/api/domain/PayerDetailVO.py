#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccountDTO import AccountDTO


class PayerDetailVO(object):

    def __init__(self):
        self._account = None
        self._pay_mode = None
        self._payer_amount = None
        self._payer_currency = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        if isinstance(value, AccountDTO):
            self._account = value
        else:
            self._account = AccountDTO.from_alipay_dict(value)
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def payer_amount(self):
        return self._payer_amount

    @payer_amount.setter
    def payer_amount(self, value):
        self._payer_amount = value
    @property
    def payer_currency(self):
        return self._payer_currency

    @payer_currency.setter
    def payer_currency(self, value):
        self._payer_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.payer_amount:
            if hasattr(self.payer_amount, 'to_alipay_dict'):
                params['payer_amount'] = self.payer_amount.to_alipay_dict()
            else:
                params['payer_amount'] = self.payer_amount
        if self.payer_currency:
            if hasattr(self.payer_currency, 'to_alipay_dict'):
                params['payer_currency'] = self.payer_currency.to_alipay_dict()
            else:
                params['payer_currency'] = self.payer_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayerDetailVO()
        if 'account' in d:
            o.account = d['account']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'payer_amount' in d:
            o.payer_amount = d['payer_amount']
        if 'payer_currency' in d:
            o.payer_currency = d['payer_currency']
        return o


