#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YLBTransDetailInfo(object):

    def __init__(self):
        self._amount = None
        self._biz_no = None
        self._memo = None
        self._trans_account_date = None
        self._trans_date = None
        self._trans_name = None
        self._trans_status = None
        self._trans_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def trans_account_date(self):
        return self._trans_account_date

    @trans_account_date.setter
    def trans_account_date(self, value):
        self._trans_account_date = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value
    @property
    def trans_name(self):
        return self._trans_name

    @trans_name.setter
    def trans_name(self, value):
        self._trans_name = value
    @property
    def trans_status(self):
        return self._trans_status

    @trans_status.setter
    def trans_status(self, value):
        self._trans_status = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.trans_account_date:
            if hasattr(self.trans_account_date, 'to_alipay_dict'):
                params['trans_account_date'] = self.trans_account_date.to_alipay_dict()
            else:
                params['trans_account_date'] = self.trans_account_date
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        if self.trans_name:
            if hasattr(self.trans_name, 'to_alipay_dict'):
                params['trans_name'] = self.trans_name.to_alipay_dict()
            else:
                params['trans_name'] = self.trans_name
        if self.trans_status:
            if hasattr(self.trans_status, 'to_alipay_dict'):
                params['trans_status'] = self.trans_status.to_alipay_dict()
            else:
                params['trans_status'] = self.trans_status
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YLBTransDetailInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'trans_account_date' in d:
            o.trans_account_date = d['trans_account_date']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        if 'trans_name' in d:
            o.trans_name = d['trans_name']
        if 'trans_status' in d:
            o.trans_status = d['trans_status']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


