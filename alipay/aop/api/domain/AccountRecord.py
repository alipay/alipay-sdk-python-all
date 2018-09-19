#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountRecord(object):

    def __init__(self):
        self._alipay_order_no = None
        self._balance = None
        self._business_type = None
        self._create_time = None
        self._in_amount = None
        self._memo = None
        self._merchant_order_no = None
        self._opt_user_id = None
        self._out_amount = None
        self._self_user_id = None
        self._type = None

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
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def in_amount(self):
        return self._in_amount

    @in_amount.setter
    def in_amount(self, value):
        self._in_amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def opt_user_id(self):
        return self._opt_user_id

    @opt_user_id.setter
    def opt_user_id(self, value):
        self._opt_user_id = value
    @property
    def out_amount(self):
        return self._out_amount

    @out_amount.setter
    def out_amount(self, value):
        self._out_amount = value
    @property
    def self_user_id(self):
        return self._self_user_id

    @self_user_id.setter
    def self_user_id(self, value):
        self._self_user_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.in_amount:
            if hasattr(self.in_amount, 'to_alipay_dict'):
                params['in_amount'] = self.in_amount.to_alipay_dict()
            else:
                params['in_amount'] = self.in_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.opt_user_id:
            if hasattr(self.opt_user_id, 'to_alipay_dict'):
                params['opt_user_id'] = self.opt_user_id.to_alipay_dict()
            else:
                params['opt_user_id'] = self.opt_user_id
        if self.out_amount:
            if hasattr(self.out_amount, 'to_alipay_dict'):
                params['out_amount'] = self.out_amount.to_alipay_dict()
            else:
                params['out_amount'] = self.out_amount
        if self.self_user_id:
            if hasattr(self.self_user_id, 'to_alipay_dict'):
                params['self_user_id'] = self.self_user_id.to_alipay_dict()
            else:
                params['self_user_id'] = self.self_user_id
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
        o = AccountRecord()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'balance' in d:
            o.balance = d['balance']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'in_amount' in d:
            o.in_amount = d['in_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'opt_user_id' in d:
            o.opt_user_id = d['opt_user_id']
        if 'out_amount' in d:
            o.out_amount = d['out_amount']
        if 'self_user_id' in d:
            o.self_user_id = d['self_user_id']
        if 'type' in d:
            o.type = d['type']
        return o


