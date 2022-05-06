#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountingLogVO(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._action = None
        self._balance = None
        self._log_id = None
        self._order_no = None
        self._other_account = None
        self._out_request_no = None
        self._trans_amount = None
        self._trans_dt = None
        self._trans_memo = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def other_account(self):
        return self._other_account

    @other_account.setter
    def other_account(self, value):
        self._other_account = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.log_id:
            if hasattr(self.log_id, 'to_alipay_dict'):
                params['log_id'] = self.log_id.to_alipay_dict()
            else:
                params['log_id'] = self.log_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.other_account:
            if hasattr(self.other_account, 'to_alipay_dict'):
                params['other_account'] = self.other_account.to_alipay_dict()
            else:
                params['other_account'] = self.other_account
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
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
        o = AccountingLogVO()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'action' in d:
            o.action = d['action']
        if 'balance' in d:
            o.balance = d['balance']
        if 'log_id' in d:
            o.log_id = d['log_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'other_account' in d:
            o.other_account = d['other_account']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o


