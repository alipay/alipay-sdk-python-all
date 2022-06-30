#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelectedBillInfo(object):

    def __init__(self):
        self._bill_id = None
        self._billkey = None
        self._cache_key = None
        self._pay_amount = None

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value
    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_id:
            if hasattr(self.bill_id, 'to_alipay_dict'):
                params['bill_id'] = self.bill_id.to_alipay_dict()
            else:
                params['bill_id'] = self.bill_id
        if self.billkey:
            if hasattr(self.billkey, 'to_alipay_dict'):
                params['billkey'] = self.billkey.to_alipay_dict()
            else:
                params['billkey'] = self.billkey
        if self.cache_key:
            if hasattr(self.cache_key, 'to_alipay_dict'):
                params['cache_key'] = self.cache_key.to_alipay_dict()
            else:
                params['cache_key'] = self.cache_key
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SelectedBillInfo()
        if 'bill_id' in d:
            o.bill_id = d['bill_id']
        if 'billkey' in d:
            o.billkey = d['billkey']
        if 'cache_key' in d:
            o.cache_key = d['cache_key']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        return o


