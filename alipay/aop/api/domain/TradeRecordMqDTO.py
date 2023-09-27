#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeRecordMqDTO(object):

    def __init__(self):
        self._account_no = None
        self._account_no_ex = None
        self._balance = None
        self._biz_name = None
        self._biz_ref_no = None
        self._biz_summary = None
        self._charges_amount = None
        self._charges_currency_type = None
        self._credit_amount = None
        self._currency_type = None
        self._debit_amount = None
        self._exchange_rate = None
        self._other_side_account_name = None
        self._other_side_account_no = None
        self._other_side_currency_type = None
        self._other_summary = None
        self._payment_amount = None
        self._payment_currency_type = None
        self._process_no = None
        self._purpose = None
        self._summary = None
        self._sync_date = None
        self._test_mode = None
        self._trade_date = None
        self._trade_no = None
        self._trade_type = None
        self._unique_no = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_no_ex(self):
        return self._account_no_ex

    @account_no_ex.setter
    def account_no_ex(self, value):
        self._account_no_ex = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_ref_no(self):
        return self._biz_ref_no

    @biz_ref_no.setter
    def biz_ref_no(self, value):
        self._biz_ref_no = value
    @property
    def biz_summary(self):
        return self._biz_summary

    @biz_summary.setter
    def biz_summary(self, value):
        self._biz_summary = value
    @property
    def charges_amount(self):
        return self._charges_amount

    @charges_amount.setter
    def charges_amount(self, value):
        self._charges_amount = value
    @property
    def charges_currency_type(self):
        return self._charges_currency_type

    @charges_currency_type.setter
    def charges_currency_type(self, value):
        self._charges_currency_type = value
    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def currency_type(self):
        return self._currency_type

    @currency_type.setter
    def currency_type(self, value):
        self._currency_type = value
    @property
    def debit_amount(self):
        return self._debit_amount

    @debit_amount.setter
    def debit_amount(self, value):
        self._debit_amount = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def other_side_account_name(self):
        return self._other_side_account_name

    @other_side_account_name.setter
    def other_side_account_name(self, value):
        self._other_side_account_name = value
    @property
    def other_side_account_no(self):
        return self._other_side_account_no

    @other_side_account_no.setter
    def other_side_account_no(self, value):
        self._other_side_account_no = value
    @property
    def other_side_currency_type(self):
        return self._other_side_currency_type

    @other_side_currency_type.setter
    def other_side_currency_type(self, value):
        self._other_side_currency_type = value
    @property
    def other_summary(self):
        return self._other_summary

    @other_summary.setter
    def other_summary(self, value):
        self._other_summary = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_currency_type(self):
        return self._payment_currency_type

    @payment_currency_type.setter
    def payment_currency_type(self, value):
        self._payment_currency_type = value
    @property
    def process_no(self):
        return self._process_no

    @process_no.setter
    def process_no(self, value):
        self._process_no = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def sync_date(self):
        return self._sync_date

    @sync_date.setter
    def sync_date(self, value):
        self._sync_date = value
    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, value):
        self._test_mode = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def unique_no(self):
        return self._unique_no

    @unique_no.setter
    def unique_no(self, value):
        self._unique_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_no_ex:
            if hasattr(self.account_no_ex, 'to_alipay_dict'):
                params['account_no_ex'] = self.account_no_ex.to_alipay_dict()
            else:
                params['account_no_ex'] = self.account_no_ex
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.biz_ref_no:
            if hasattr(self.biz_ref_no, 'to_alipay_dict'):
                params['biz_ref_no'] = self.biz_ref_no.to_alipay_dict()
            else:
                params['biz_ref_no'] = self.biz_ref_no
        if self.biz_summary:
            if hasattr(self.biz_summary, 'to_alipay_dict'):
                params['biz_summary'] = self.biz_summary.to_alipay_dict()
            else:
                params['biz_summary'] = self.biz_summary
        if self.charges_amount:
            if hasattr(self.charges_amount, 'to_alipay_dict'):
                params['charges_amount'] = self.charges_amount.to_alipay_dict()
            else:
                params['charges_amount'] = self.charges_amount
        if self.charges_currency_type:
            if hasattr(self.charges_currency_type, 'to_alipay_dict'):
                params['charges_currency_type'] = self.charges_currency_type.to_alipay_dict()
            else:
                params['charges_currency_type'] = self.charges_currency_type
        if self.credit_amount:
            if hasattr(self.credit_amount, 'to_alipay_dict'):
                params['credit_amount'] = self.credit_amount.to_alipay_dict()
            else:
                params['credit_amount'] = self.credit_amount
        if self.currency_type:
            if hasattr(self.currency_type, 'to_alipay_dict'):
                params['currency_type'] = self.currency_type.to_alipay_dict()
            else:
                params['currency_type'] = self.currency_type
        if self.debit_amount:
            if hasattr(self.debit_amount, 'to_alipay_dict'):
                params['debit_amount'] = self.debit_amount.to_alipay_dict()
            else:
                params['debit_amount'] = self.debit_amount
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.other_side_account_name:
            if hasattr(self.other_side_account_name, 'to_alipay_dict'):
                params['other_side_account_name'] = self.other_side_account_name.to_alipay_dict()
            else:
                params['other_side_account_name'] = self.other_side_account_name
        if self.other_side_account_no:
            if hasattr(self.other_side_account_no, 'to_alipay_dict'):
                params['other_side_account_no'] = self.other_side_account_no.to_alipay_dict()
            else:
                params['other_side_account_no'] = self.other_side_account_no
        if self.other_side_currency_type:
            if hasattr(self.other_side_currency_type, 'to_alipay_dict'):
                params['other_side_currency_type'] = self.other_side_currency_type.to_alipay_dict()
            else:
                params['other_side_currency_type'] = self.other_side_currency_type
        if self.other_summary:
            if hasattr(self.other_summary, 'to_alipay_dict'):
                params['other_summary'] = self.other_summary.to_alipay_dict()
            else:
                params['other_summary'] = self.other_summary
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_currency_type:
            if hasattr(self.payment_currency_type, 'to_alipay_dict'):
                params['payment_currency_type'] = self.payment_currency_type.to_alipay_dict()
            else:
                params['payment_currency_type'] = self.payment_currency_type
        if self.process_no:
            if hasattr(self.process_no, 'to_alipay_dict'):
                params['process_no'] = self.process_no.to_alipay_dict()
            else:
                params['process_no'] = self.process_no
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.sync_date:
            if hasattr(self.sync_date, 'to_alipay_dict'):
                params['sync_date'] = self.sync_date.to_alipay_dict()
            else:
                params['sync_date'] = self.sync_date
        if self.test_mode:
            if hasattr(self.test_mode, 'to_alipay_dict'):
                params['test_mode'] = self.test_mode.to_alipay_dict()
            else:
                params['test_mode'] = self.test_mode
        if self.trade_date:
            if hasattr(self.trade_date, 'to_alipay_dict'):
                params['trade_date'] = self.trade_date.to_alipay_dict()
            else:
                params['trade_date'] = self.trade_date
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.unique_no:
            if hasattr(self.unique_no, 'to_alipay_dict'):
                params['unique_no'] = self.unique_no.to_alipay_dict()
            else:
                params['unique_no'] = self.unique_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeRecordMqDTO()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_no_ex' in d:
            o.account_no_ex = d['account_no_ex']
        if 'balance' in d:
            o.balance = d['balance']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'biz_ref_no' in d:
            o.biz_ref_no = d['biz_ref_no']
        if 'biz_summary' in d:
            o.biz_summary = d['biz_summary']
        if 'charges_amount' in d:
            o.charges_amount = d['charges_amount']
        if 'charges_currency_type' in d:
            o.charges_currency_type = d['charges_currency_type']
        if 'credit_amount' in d:
            o.credit_amount = d['credit_amount']
        if 'currency_type' in d:
            o.currency_type = d['currency_type']
        if 'debit_amount' in d:
            o.debit_amount = d['debit_amount']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'other_side_account_name' in d:
            o.other_side_account_name = d['other_side_account_name']
        if 'other_side_account_no' in d:
            o.other_side_account_no = d['other_side_account_no']
        if 'other_side_currency_type' in d:
            o.other_side_currency_type = d['other_side_currency_type']
        if 'other_summary' in d:
            o.other_summary = d['other_summary']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_currency_type' in d:
            o.payment_currency_type = d['payment_currency_type']
        if 'process_no' in d:
            o.process_no = d['process_no']
        if 'purpose' in d:
            o.purpose = d['purpose']
        if 'summary' in d:
            o.summary = d['summary']
        if 'sync_date' in d:
            o.sync_date = d['sync_date']
        if 'test_mode' in d:
            o.test_mode = d['test_mode']
        if 'trade_date' in d:
            o.trade_date = d['trade_date']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'unique_no' in d:
            o.unique_no = d['unique_no']
        return o


