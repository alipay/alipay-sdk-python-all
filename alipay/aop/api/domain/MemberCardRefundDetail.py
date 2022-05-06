#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardRefundDetail(object):

    def __init__(self):
        self._balance = None
        self._order_id = None
        self._principal_balance = None
        self._record_time = None
        self._refund_amount = None
        self._refund_benefit_amount = None
        self._subtract_benefit_amount = None
        self._subtract_discount_amount = None
        self._subtract_voucher_amount = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def principal_balance(self):
        return self._principal_balance

    @principal_balance.setter
    def principal_balance(self, value):
        self._principal_balance = value
    @property
    def record_time(self):
        return self._record_time

    @record_time.setter
    def record_time(self, value):
        self._record_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_benefit_amount(self):
        return self._refund_benefit_amount

    @refund_benefit_amount.setter
    def refund_benefit_amount(self, value):
        self._refund_benefit_amount = value
    @property
    def subtract_benefit_amount(self):
        return self._subtract_benefit_amount

    @subtract_benefit_amount.setter
    def subtract_benefit_amount(self, value):
        self._subtract_benefit_amount = value
    @property
    def subtract_discount_amount(self):
        return self._subtract_discount_amount

    @subtract_discount_amount.setter
    def subtract_discount_amount(self, value):
        self._subtract_discount_amount = value
    @property
    def subtract_voucher_amount(self):
        return self._subtract_voucher_amount

    @subtract_voucher_amount.setter
    def subtract_voucher_amount(self, value):
        self._subtract_voucher_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.principal_balance:
            if hasattr(self.principal_balance, 'to_alipay_dict'):
                params['principal_balance'] = self.principal_balance.to_alipay_dict()
            else:
                params['principal_balance'] = self.principal_balance
        if self.record_time:
            if hasattr(self.record_time, 'to_alipay_dict'):
                params['record_time'] = self.record_time.to_alipay_dict()
            else:
                params['record_time'] = self.record_time
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_benefit_amount:
            if hasattr(self.refund_benefit_amount, 'to_alipay_dict'):
                params['refund_benefit_amount'] = self.refund_benefit_amount.to_alipay_dict()
            else:
                params['refund_benefit_amount'] = self.refund_benefit_amount
        if self.subtract_benefit_amount:
            if hasattr(self.subtract_benefit_amount, 'to_alipay_dict'):
                params['subtract_benefit_amount'] = self.subtract_benefit_amount.to_alipay_dict()
            else:
                params['subtract_benefit_amount'] = self.subtract_benefit_amount
        if self.subtract_discount_amount:
            if hasattr(self.subtract_discount_amount, 'to_alipay_dict'):
                params['subtract_discount_amount'] = self.subtract_discount_amount.to_alipay_dict()
            else:
                params['subtract_discount_amount'] = self.subtract_discount_amount
        if self.subtract_voucher_amount:
            if hasattr(self.subtract_voucher_amount, 'to_alipay_dict'):
                params['subtract_voucher_amount'] = self.subtract_voucher_amount.to_alipay_dict()
            else:
                params['subtract_voucher_amount'] = self.subtract_voucher_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardRefundDetail()
        if 'balance' in d:
            o.balance = d['balance']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'principal_balance' in d:
            o.principal_balance = d['principal_balance']
        if 'record_time' in d:
            o.record_time = d['record_time']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_benefit_amount' in d:
            o.refund_benefit_amount = d['refund_benefit_amount']
        if 'subtract_benefit_amount' in d:
            o.subtract_benefit_amount = d['subtract_benefit_amount']
        if 'subtract_discount_amount' in d:
            o.subtract_discount_amount = d['subtract_discount_amount']
        if 'subtract_voucher_amount' in d:
            o.subtract_voucher_amount = d['subtract_voucher_amount']
        return o


