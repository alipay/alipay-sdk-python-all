#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstBillInfo(object):

    def __init__(self):
        self._balance = None
        self._bill_amount = None
        self._bill_date = None
        self._bill_id = None
        self._cache_key = None
        self._charge_type = None
        self._fine_amount = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value
    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def fine_amount(self):
        return self._fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self._fine_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_id:
            if hasattr(self.bill_id, 'to_alipay_dict'):
                params['bill_id'] = self.bill_id.to_alipay_dict()
            else:
                params['bill_id'] = self.bill_id
        if self.cache_key:
            if hasattr(self.cache_key, 'to_alipay_dict'):
                params['cache_key'] = self.cache_key.to_alipay_dict()
            else:
                params['cache_key'] = self.cache_key
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.fine_amount:
            if hasattr(self.fine_amount, 'to_alipay_dict'):
                params['fine_amount'] = self.fine_amount.to_alipay_dict()
            else:
                params['fine_amount'] = self.fine_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstBillInfo()
        if 'balance' in d:
            o.balance = d['balance']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_id' in d:
            o.bill_id = d['bill_id']
        if 'cache_key' in d:
            o.cache_key = d['cache_key']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'fine_amount' in d:
            o.fine_amount = d['fine_amount']
        return o


