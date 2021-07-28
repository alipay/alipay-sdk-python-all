#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountLogItemResult(object):

    def __init__(self):
        self._account_log_id = None
        self._alipay_order_no = None
        self._balance = None
        self._bill_source = None
        self._biz_desc = None
        self._biz_nos = None
        self._biz_orig_no = None
        self._direction = None
        self._merchant_order_no = None
        self._other_account = None
        self._trans_amount = None
        self._trans_dt = None
        self._trans_memo = None
        self._type = None

    @property
    def account_log_id(self):
        return self._account_log_id

    @account_log_id.setter
    def account_log_id(self, value):
        self._account_log_id = value
    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def bill_source(self):
        return self._bill_source

    @bill_source.setter
    def bill_source(self, value):
        self._bill_source = value
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_nos(self):
        return self._biz_nos

    @biz_nos.setter
    def biz_nos(self, value):
        self._biz_nos = value
    @property
    def biz_orig_no(self):
        return self._biz_orig_no

    @biz_orig_no.setter
    def biz_orig_no(self, value):
        self._biz_orig_no = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def other_account(self):
        return self._other_account

    @other_account.setter
    def other_account(self, value):
        self._other_account = value
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
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_log_id:
            if hasattr(self.account_log_id, 'to_alipay_dict'):
                params['account_log_id'] = self.account_log_id.to_alipay_dict()
            else:
                params['account_log_id'] = self.account_log_id
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.bill_source:
            if hasattr(self.bill_source, 'to_alipay_dict'):
                params['bill_source'] = self.bill_source.to_alipay_dict()
            else:
                params['bill_source'] = self.bill_source
        if self.biz_desc:
            if hasattr(self.biz_desc, 'to_alipay_dict'):
                params['biz_desc'] = self.biz_desc.to_alipay_dict()
            else:
                params['biz_desc'] = self.biz_desc
        if self.biz_nos:
            if hasattr(self.biz_nos, 'to_alipay_dict'):
                params['biz_nos'] = self.biz_nos.to_alipay_dict()
            else:
                params['biz_nos'] = self.biz_nos
        if self.biz_orig_no:
            if hasattr(self.biz_orig_no, 'to_alipay_dict'):
                params['biz_orig_no'] = self.biz_orig_no.to_alipay_dict()
            else:
                params['biz_orig_no'] = self.biz_orig_no
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.other_account:
            if hasattr(self.other_account, 'to_alipay_dict'):
                params['other_account'] = self.other_account.to_alipay_dict()
            else:
                params['other_account'] = self.other_account
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountLogItemResult()
        if 'account_log_id' in d:
            o.account_log_id = d['account_log_id']
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'balance' in d:
            o.balance = d['balance']
        if 'bill_source' in d:
            o.bill_source = d['bill_source']
        if 'biz_desc' in d:
            o.biz_desc = d['biz_desc']
        if 'biz_nos' in d:
            o.biz_nos = d['biz_nos']
        if 'biz_orig_no' in d:
            o.biz_orig_no = d['biz_orig_no']
        if 'direction' in d:
            o.direction = d['direction']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'other_account' in d:
            o.other_account = d['other_account']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        if 'type' in d:
            o.type = d['type']
        return o


