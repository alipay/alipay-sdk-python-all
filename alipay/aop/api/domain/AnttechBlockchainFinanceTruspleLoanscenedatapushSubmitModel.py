#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceTruspleLoanscenedatapushSubmitModel(object):

    def __init__(self):
        self._currency = None
        self._loan_amount = None
        self._login_id = None
        self._memo = None
        self._out_biz_id = None
        self._receiver_account_no = None
        self._receiver_bank_code = None
        self._receiver_name = None
        self._request_id = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def receiver_account_no(self):
        return self._receiver_account_no

    @receiver_account_no.setter
    def receiver_account_no(self, value):
        self._receiver_account_no = value
    @property
    def receiver_bank_code(self):
        return self._receiver_bank_code

    @receiver_bank_code.setter
    def receiver_bank_code(self, value):
        self._receiver_bank_code = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.receiver_account_no:
            if hasattr(self.receiver_account_no, 'to_alipay_dict'):
                params['receiver_account_no'] = self.receiver_account_no.to_alipay_dict()
            else:
                params['receiver_account_no'] = self.receiver_account_no
        if self.receiver_bank_code:
            if hasattr(self.receiver_bank_code, 'to_alipay_dict'):
                params['receiver_bank_code'] = self.receiver_bank_code.to_alipay_dict()
            else:
                params['receiver_bank_code'] = self.receiver_bank_code
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleLoanscenedatapushSubmitModel()
        if 'currency' in d:
            o.currency = d['currency']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'receiver_account_no' in d:
            o.receiver_account_no = d['receiver_account_no']
        if 'receiver_bank_code' in d:
            o.receiver_bank_code = d['receiver_bank_code']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


