#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleDetailResponse(object):

    def __init__(self):
        self._amount = None
        self._id = None
        self._rate = None
        self._settle_order_id = None
        self._settle_time = None
        self._trans_in_account = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def settle_order_id(self):
        return self._settle_order_id

    @settle_order_id.setter
    def settle_order_id(self, value):
        self._settle_order_id = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def trans_in_account(self):
        return self._trans_in_account

    @trans_in_account.setter
    def trans_in_account(self, value):
        self._trans_in_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.settle_order_id:
            if hasattr(self.settle_order_id, 'to_alipay_dict'):
                params['settle_order_id'] = self.settle_order_id.to_alipay_dict()
            else:
                params['settle_order_id'] = self.settle_order_id
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.trans_in_account:
            if hasattr(self.trans_in_account, 'to_alipay_dict'):
                params['trans_in_account'] = self.trans_in_account.to_alipay_dict()
            else:
                params['trans_in_account'] = self.trans_in_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleDetailResponse()
        if 'amount' in d:
            o.amount = d['amount']
        if 'id' in d:
            o.id = d['id']
        if 'rate' in d:
            o.rate = d['rate']
        if 'settle_order_id' in d:
            o.settle_order_id = d['settle_order_id']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'trans_in_account' in d:
            o.trans_in_account = d['trans_in_account']
        return o


