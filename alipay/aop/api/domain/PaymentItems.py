#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class PaymentItems(object):

    def __init__(self):
        self._allowd_partial_payment = None
        self._payment_item_end_time = None
        self._payment_item_id = None
        self._payment_item_local_name = None
        self._payment_item_name = None
        self._payment_start_time = None
        self._payment_total_amount = None

    @property
    def allowd_partial_payment(self):
        return self._allowd_partial_payment

    @allowd_partial_payment.setter
    def allowd_partial_payment(self, value):
        self._allowd_partial_payment = value
    @property
    def payment_item_end_time(self):
        return self._payment_item_end_time

    @payment_item_end_time.setter
    def payment_item_end_time(self, value):
        self._payment_item_end_time = value
    @property
    def payment_item_id(self):
        return self._payment_item_id

    @payment_item_id.setter
    def payment_item_id(self, value):
        self._payment_item_id = value
    @property
    def payment_item_local_name(self):
        return self._payment_item_local_name

    @payment_item_local_name.setter
    def payment_item_local_name(self, value):
        self._payment_item_local_name = value
    @property
    def payment_item_name(self):
        return self._payment_item_name

    @payment_item_name.setter
    def payment_item_name(self, value):
        self._payment_item_name = value
    @property
    def payment_start_time(self):
        return self._payment_start_time

    @payment_start_time.setter
    def payment_start_time(self, value):
        self._payment_start_time = value
    @property
    def payment_total_amount(self):
        return self._payment_total_amount

    @payment_total_amount.setter
    def payment_total_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._payment_total_amount = value
        else:
            self._payment_total_amount = TuitionMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.allowd_partial_payment:
            if hasattr(self.allowd_partial_payment, 'to_alipay_dict'):
                params['allowd_partial_payment'] = self.allowd_partial_payment.to_alipay_dict()
            else:
                params['allowd_partial_payment'] = self.allowd_partial_payment
        if self.payment_item_end_time:
            if hasattr(self.payment_item_end_time, 'to_alipay_dict'):
                params['payment_item_end_time'] = self.payment_item_end_time.to_alipay_dict()
            else:
                params['payment_item_end_time'] = self.payment_item_end_time
        if self.payment_item_id:
            if hasattr(self.payment_item_id, 'to_alipay_dict'):
                params['payment_item_id'] = self.payment_item_id.to_alipay_dict()
            else:
                params['payment_item_id'] = self.payment_item_id
        if self.payment_item_local_name:
            if hasattr(self.payment_item_local_name, 'to_alipay_dict'):
                params['payment_item_local_name'] = self.payment_item_local_name.to_alipay_dict()
            else:
                params['payment_item_local_name'] = self.payment_item_local_name
        if self.payment_item_name:
            if hasattr(self.payment_item_name, 'to_alipay_dict'):
                params['payment_item_name'] = self.payment_item_name.to_alipay_dict()
            else:
                params['payment_item_name'] = self.payment_item_name
        if self.payment_start_time:
            if hasattr(self.payment_start_time, 'to_alipay_dict'):
                params['payment_start_time'] = self.payment_start_time.to_alipay_dict()
            else:
                params['payment_start_time'] = self.payment_start_time
        if self.payment_total_amount:
            if hasattr(self.payment_total_amount, 'to_alipay_dict'):
                params['payment_total_amount'] = self.payment_total_amount.to_alipay_dict()
            else:
                params['payment_total_amount'] = self.payment_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentItems()
        if 'allowd_partial_payment' in d:
            o.allowd_partial_payment = d['allowd_partial_payment']
        if 'payment_item_end_time' in d:
            o.payment_item_end_time = d['payment_item_end_time']
        if 'payment_item_id' in d:
            o.payment_item_id = d['payment_item_id']
        if 'payment_item_local_name' in d:
            o.payment_item_local_name = d['payment_item_local_name']
        if 'payment_item_name' in d:
            o.payment_item_name = d['payment_item_name']
        if 'payment_start_time' in d:
            o.payment_start_time = d['payment_start_time']
        if 'payment_total_amount' in d:
            o.payment_total_amount = d['payment_total_amount']
        return o


