#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSubscriptionMigrateModel(object):

    def __init__(self):
        self._agreement_no = None
        self._customer_id = None
        self._period_end = None
        self._period_paid_amount = None
        self._period_start = None
        self._period_trade_no = None
        self._price_id = None
        self._target_app_id = None
        self._target_pid = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def period_end(self):
        return self._period_end

    @period_end.setter
    def period_end(self, value):
        self._period_end = value
    @property
    def period_paid_amount(self):
        return self._period_paid_amount

    @period_paid_amount.setter
    def period_paid_amount(self, value):
        self._period_paid_amount = value
    @property
    def period_start(self):
        return self._period_start

    @period_start.setter
    def period_start(self, value):
        self._period_start = value
    @property
    def period_trade_no(self):
        return self._period_trade_no

    @period_trade_no.setter
    def period_trade_no(self, value):
        self._period_trade_no = value
    @property
    def price_id(self):
        return self._price_id

    @price_id.setter
    def price_id(self, value):
        self._price_id = value
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value
    @property
    def target_pid(self):
        return self._target_pid

    @target_pid.setter
    def target_pid(self, value):
        self._target_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.period_end:
            if hasattr(self.period_end, 'to_alipay_dict'):
                params['period_end'] = self.period_end.to_alipay_dict()
            else:
                params['period_end'] = self.period_end
        if self.period_paid_amount:
            if hasattr(self.period_paid_amount, 'to_alipay_dict'):
                params['period_paid_amount'] = self.period_paid_amount.to_alipay_dict()
            else:
                params['period_paid_amount'] = self.period_paid_amount
        if self.period_start:
            if hasattr(self.period_start, 'to_alipay_dict'):
                params['period_start'] = self.period_start.to_alipay_dict()
            else:
                params['period_start'] = self.period_start
        if self.period_trade_no:
            if hasattr(self.period_trade_no, 'to_alipay_dict'):
                params['period_trade_no'] = self.period_trade_no.to_alipay_dict()
            else:
                params['period_trade_no'] = self.period_trade_no
        if self.price_id:
            if hasattr(self.price_id, 'to_alipay_dict'):
                params['price_id'] = self.price_id.to_alipay_dict()
            else:
                params['price_id'] = self.price_id
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        if self.target_pid:
            if hasattr(self.target_pid, 'to_alipay_dict'):
                params['target_pid'] = self.target_pid.to_alipay_dict()
            else:
                params['target_pid'] = self.target_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSubscriptionMigrateModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'period_end' in d:
            o.period_end = d['period_end']
        if 'period_paid_amount' in d:
            o.period_paid_amount = d['period_paid_amount']
        if 'period_start' in d:
            o.period_start = d['period_start']
        if 'period_trade_no' in d:
            o.period_trade_no = d['period_trade_no']
        if 'price_id' in d:
            o.price_id = d['price_id']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        if 'target_pid' in d:
            o.target_pid = d['target_pid']
        return o


