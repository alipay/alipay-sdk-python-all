#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CbClaimBill(object):

    def __init__(self):
        self._claim_amount = None
        self._claim_no = None
        self._company_type = None
        self._open_id = None
        self._payer_account_type = None
        self._transaction_currency = None
        self._transaction_id = None
        self._transaction_time = None
        self._user_id = None

    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def transaction_currency(self):
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, value):
        self._transaction_currency = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def transaction_time(self):
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self._transaction_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.transaction_currency:
            if hasattr(self.transaction_currency, 'to_alipay_dict'):
                params['transaction_currency'] = self.transaction_currency.to_alipay_dict()
            else:
                params['transaction_currency'] = self.transaction_currency
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        if self.transaction_time:
            if hasattr(self.transaction_time, 'to_alipay_dict'):
                params['transaction_time'] = self.transaction_time.to_alipay_dict()
            else:
                params['transaction_time'] = self.transaction_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CbClaimBill()
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'transaction_currency' in d:
            o.transaction_currency = d['transaction_currency']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'transaction_time' in d:
            o.transaction_time = d['transaction_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


