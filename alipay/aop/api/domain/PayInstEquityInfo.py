#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInstEquityInfo(object):

    def __init__(self):
        self._available_begin_time = None
        self._available_end_time = None
        self._campaign_id = None
        self._discount_amount = None
        self._send_order_id = None
        self._status = None
        self._threshold_amount = None
        self._transaction_id = None
        self._user_id = None

    @property
    def available_begin_time(self):
        return self._available_begin_time

    @available_begin_time.setter
    def available_begin_time(self, value):
        self._available_begin_time = value
    @property
    def available_end_time(self):
        return self._available_end_time

    @available_end_time.setter
    def available_end_time(self, value):
        self._available_end_time = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_begin_time:
            if hasattr(self.available_begin_time, 'to_alipay_dict'):
                params['available_begin_time'] = self.available_begin_time.to_alipay_dict()
            else:
                params['available_begin_time'] = self.available_begin_time
        if self.available_end_time:
            if hasattr(self.available_end_time, 'to_alipay_dict'):
                params['available_end_time'] = self.available_end_time.to_alipay_dict()
            else:
                params['available_end_time'] = self.available_end_time
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayInstEquityInfo()
        if 'available_begin_time' in d:
            o.available_begin_time = d['available_begin_time']
        if 'available_end_time' in d:
            o.available_end_time = d['available_end_time']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'status' in d:
            o.status = d['status']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


