#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmountTypeSyncData(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_desc = None
        self._has_alipay_trade = None
        self._task_amount = None
        self._task_desc = None
        self._trade_no = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def has_alipay_trade(self):
        return self._has_alipay_trade

    @has_alipay_trade.setter
    def has_alipay_trade(self, value):
        self._has_alipay_trade = value
    @property
    def task_amount(self):
        return self._task_amount

    @task_amount.setter
    def task_amount(self, value):
        self._task_amount = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.has_alipay_trade:
            if hasattr(self.has_alipay_trade, 'to_alipay_dict'):
                params['has_alipay_trade'] = self.has_alipay_trade.to_alipay_dict()
            else:
                params['has_alipay_trade'] = self.has_alipay_trade
        if self.task_amount:
            if hasattr(self.task_amount, 'to_alipay_dict'):
                params['task_amount'] = self.task_amount.to_alipay_dict()
            else:
                params['task_amount'] = self.task_amount
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmountTypeSyncData()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'has_alipay_trade' in d:
            o.has_alipay_trade = d['has_alipay_trade']
        if 'task_amount' in d:
            o.task_amount = d['task_amount']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


