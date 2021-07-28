#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferAmount import TransferAmount


class TransferPaymentItem(object):

    def __init__(self):
        self._channel_accept_time = None
        self._channel_remit_time = None
        self._mandatory_payment = None
        self._partial_allowed = None
        self._payment_completed = None
        self._payment_item_amount = None
        self._payment_item_id = None
        self._payment_item_name = None
        self._payment_item_type = None
        self._payment_local_name = None

    @property
    def channel_accept_time(self):
        return self._channel_accept_time

    @channel_accept_time.setter
    def channel_accept_time(self, value):
        self._channel_accept_time = value
    @property
    def channel_remit_time(self):
        return self._channel_remit_time

    @channel_remit_time.setter
    def channel_remit_time(self, value):
        self._channel_remit_time = value
    @property
    def mandatory_payment(self):
        return self._mandatory_payment

    @mandatory_payment.setter
    def mandatory_payment(self, value):
        self._mandatory_payment = value
    @property
    def partial_allowed(self):
        return self._partial_allowed

    @partial_allowed.setter
    def partial_allowed(self, value):
        self._partial_allowed = value
    @property
    def payment_completed(self):
        return self._payment_completed

    @payment_completed.setter
    def payment_completed(self, value):
        self._payment_completed = value
    @property
    def payment_item_amount(self):
        return self._payment_item_amount

    @payment_item_amount.setter
    def payment_item_amount(self, value):
        if isinstance(value, TransferAmount):
            self._payment_item_amount = value
        else:
            self._payment_item_amount = TransferAmount.from_alipay_dict(value)
    @property
    def payment_item_id(self):
        return self._payment_item_id

    @payment_item_id.setter
    def payment_item_id(self, value):
        self._payment_item_id = value
    @property
    def payment_item_name(self):
        return self._payment_item_name

    @payment_item_name.setter
    def payment_item_name(self, value):
        self._payment_item_name = value
    @property
    def payment_item_type(self):
        return self._payment_item_type

    @payment_item_type.setter
    def payment_item_type(self, value):
        self._payment_item_type = value
    @property
    def payment_local_name(self):
        return self._payment_local_name

    @payment_local_name.setter
    def payment_local_name(self, value):
        self._payment_local_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_accept_time:
            if hasattr(self.channel_accept_time, 'to_alipay_dict'):
                params['channel_accept_time'] = self.channel_accept_time.to_alipay_dict()
            else:
                params['channel_accept_time'] = self.channel_accept_time
        if self.channel_remit_time:
            if hasattr(self.channel_remit_time, 'to_alipay_dict'):
                params['channel_remit_time'] = self.channel_remit_time.to_alipay_dict()
            else:
                params['channel_remit_time'] = self.channel_remit_time
        if self.mandatory_payment:
            if hasattr(self.mandatory_payment, 'to_alipay_dict'):
                params['mandatory_payment'] = self.mandatory_payment.to_alipay_dict()
            else:
                params['mandatory_payment'] = self.mandatory_payment
        if self.partial_allowed:
            if hasattr(self.partial_allowed, 'to_alipay_dict'):
                params['partial_allowed'] = self.partial_allowed.to_alipay_dict()
            else:
                params['partial_allowed'] = self.partial_allowed
        if self.payment_completed:
            if hasattr(self.payment_completed, 'to_alipay_dict'):
                params['payment_completed'] = self.payment_completed.to_alipay_dict()
            else:
                params['payment_completed'] = self.payment_completed
        if self.payment_item_amount:
            if hasattr(self.payment_item_amount, 'to_alipay_dict'):
                params['payment_item_amount'] = self.payment_item_amount.to_alipay_dict()
            else:
                params['payment_item_amount'] = self.payment_item_amount
        if self.payment_item_id:
            if hasattr(self.payment_item_id, 'to_alipay_dict'):
                params['payment_item_id'] = self.payment_item_id.to_alipay_dict()
            else:
                params['payment_item_id'] = self.payment_item_id
        if self.payment_item_name:
            if hasattr(self.payment_item_name, 'to_alipay_dict'):
                params['payment_item_name'] = self.payment_item_name.to_alipay_dict()
            else:
                params['payment_item_name'] = self.payment_item_name
        if self.payment_item_type:
            if hasattr(self.payment_item_type, 'to_alipay_dict'):
                params['payment_item_type'] = self.payment_item_type.to_alipay_dict()
            else:
                params['payment_item_type'] = self.payment_item_type
        if self.payment_local_name:
            if hasattr(self.payment_local_name, 'to_alipay_dict'):
                params['payment_local_name'] = self.payment_local_name.to_alipay_dict()
            else:
                params['payment_local_name'] = self.payment_local_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferPaymentItem()
        if 'channel_accept_time' in d:
            o.channel_accept_time = d['channel_accept_time']
        if 'channel_remit_time' in d:
            o.channel_remit_time = d['channel_remit_time']
        if 'mandatory_payment' in d:
            o.mandatory_payment = d['mandatory_payment']
        if 'partial_allowed' in d:
            o.partial_allowed = d['partial_allowed']
        if 'payment_completed' in d:
            o.payment_completed = d['payment_completed']
        if 'payment_item_amount' in d:
            o.payment_item_amount = d['payment_item_amount']
        if 'payment_item_id' in d:
            o.payment_item_id = d['payment_item_id']
        if 'payment_item_name' in d:
            o.payment_item_name = d['payment_item_name']
        if 'payment_item_type' in d:
            o.payment_item_type = d['payment_item_type']
        if 'payment_local_name' in d:
            o.payment_local_name = d['payment_local_name']
        return o


