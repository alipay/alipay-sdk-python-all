#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeAssocBillDetails(object):

    def __init__(self):
        self._acct_period = None
        self._bill_entry_amount = None
        self._bill_entry_id = None
        self._cost_type = None

    @property
    def acct_period(self):
        return self._acct_period

    @acct_period.setter
    def acct_period(self, value):
        self._acct_period = value
    @property
    def bill_entry_amount(self):
        return self._bill_entry_amount

    @bill_entry_amount.setter
    def bill_entry_amount(self, value):
        self._bill_entry_amount = value
    @property
    def bill_entry_id(self):
        return self._bill_entry_id

    @bill_entry_id.setter
    def bill_entry_id(self, value):
        self._bill_entry_id = value
    @property
    def cost_type(self):
        return self._cost_type

    @cost_type.setter
    def cost_type(self, value):
        self._cost_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.acct_period:
            if hasattr(self.acct_period, 'to_alipay_dict'):
                params['acct_period'] = self.acct_period.to_alipay_dict()
            else:
                params['acct_period'] = self.acct_period
        if self.bill_entry_amount:
            if hasattr(self.bill_entry_amount, 'to_alipay_dict'):
                params['bill_entry_amount'] = self.bill_entry_amount.to_alipay_dict()
            else:
                params['bill_entry_amount'] = self.bill_entry_amount
        if self.bill_entry_id:
            if hasattr(self.bill_entry_id, 'to_alipay_dict'):
                params['bill_entry_id'] = self.bill_entry_id.to_alipay_dict()
            else:
                params['bill_entry_id'] = self.bill_entry_id
        if self.cost_type:
            if hasattr(self.cost_type, 'to_alipay_dict'):
                params['cost_type'] = self.cost_type.to_alipay_dict()
            else:
                params['cost_type'] = self.cost_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeAssocBillDetails()
        if 'acct_period' in d:
            o.acct_period = d['acct_period']
        if 'bill_entry_amount' in d:
            o.bill_entry_amount = d['bill_entry_amount']
        if 'bill_entry_id' in d:
            o.bill_entry_id = d['bill_entry_id']
        if 'cost_type' in d:
            o.cost_type = d['cost_type']
        return o


