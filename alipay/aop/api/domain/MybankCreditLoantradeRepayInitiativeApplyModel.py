#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Account import Account
from alipay.aop.api.domain.Member import Member


class MybankCreditLoantradeRepayInitiativeApplyModel(object):

    def __init__(self):
        self._loan_ar_no = None
        self._repay_account = None
        self._repay_amount = None
        self._repay_amount_strategy = None
        self._repay_customer = None
        self._repay_date = None
        self._request_id = None
        self._trans_memo = None

    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def repay_account(self):
        return self._repay_account

    @repay_account.setter
    def repay_account(self, value):
        if isinstance(value, Account):
            self._repay_account = value
        else:
            self._repay_account = Account.from_alipay_dict(value)
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_amount_strategy(self):
        return self._repay_amount_strategy

    @repay_amount_strategy.setter
    def repay_amount_strategy(self, value):
        self._repay_amount_strategy = value
    @property
    def repay_customer(self):
        return self._repay_customer

    @repay_customer.setter
    def repay_customer(self, value):
        if isinstance(value, Member):
            self._repay_customer = value
        else:
            self._repay_customer = Member.from_alipay_dict(value)
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.repay_account:
            if hasattr(self.repay_account, 'to_alipay_dict'):
                params['repay_account'] = self.repay_account.to_alipay_dict()
            else:
                params['repay_account'] = self.repay_account
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_amount_strategy:
            if hasattr(self.repay_amount_strategy, 'to_alipay_dict'):
                params['repay_amount_strategy'] = self.repay_amount_strategy.to_alipay_dict()
            else:
                params['repay_amount_strategy'] = self.repay_amount_strategy
        if self.repay_customer:
            if hasattr(self.repay_customer, 'to_alipay_dict'):
                params['repay_customer'] = self.repay_customer.to_alipay_dict()
            else:
                params['repay_customer'] = self.repay_customer
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.trans_memo:
            if hasattr(self.trans_memo, 'to_alipay_dict'):
                params['trans_memo'] = self.trans_memo.to_alipay_dict()
            else:
                params['trans_memo'] = self.trans_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeRepayInitiativeApplyModel()
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'repay_account' in d:
            o.repay_account = d['repay_account']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_amount_strategy' in d:
            o.repay_amount_strategy = d['repay_amount_strategy']
        if 'repay_customer' in d:
            o.repay_customer = d['repay_customer']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o


