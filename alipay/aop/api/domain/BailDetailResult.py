#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BailDetailResult(object):

    def __init__(self):
        self._amount = None
        self._bail_type = None
        self._balance = None
        self._biz_desc = None
        self._biz_orig_no = None
        self._memo = None
        self._trans_dt = None
        self._trans_log_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bail_type(self):
        return self._bail_type

    @bail_type.setter
    def bail_type(self, value):
        self._bail_type = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def biz_orig_no(self):
        return self._biz_orig_no

    @biz_orig_no.setter
    def biz_orig_no(self, value):
        self._biz_orig_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def trans_log_id(self):
        return self._trans_log_id

    @trans_log_id.setter
    def trans_log_id(self, value):
        self._trans_log_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bail_type:
            if hasattr(self.bail_type, 'to_alipay_dict'):
                params['bail_type'] = self.bail_type.to_alipay_dict()
            else:
                params['bail_type'] = self.bail_type
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.biz_desc:
            if hasattr(self.biz_desc, 'to_alipay_dict'):
                params['biz_desc'] = self.biz_desc.to_alipay_dict()
            else:
                params['biz_desc'] = self.biz_desc
        if self.biz_orig_no:
            if hasattr(self.biz_orig_no, 'to_alipay_dict'):
                params['biz_orig_no'] = self.biz_orig_no.to_alipay_dict()
            else:
                params['biz_orig_no'] = self.biz_orig_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        if self.trans_log_id:
            if hasattr(self.trans_log_id, 'to_alipay_dict'):
                params['trans_log_id'] = self.trans_log_id.to_alipay_dict()
            else:
                params['trans_log_id'] = self.trans_log_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BailDetailResult()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bail_type' in d:
            o.bail_type = d['bail_type']
        if 'balance' in d:
            o.balance = d['balance']
        if 'biz_desc' in d:
            o.biz_desc = d['biz_desc']
        if 'biz_orig_no' in d:
            o.biz_orig_no = d['biz_orig_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'trans_log_id' in d:
            o.trans_log_id = d['trans_log_id']
        return o


