#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepositBackInfo(object):

    def __init__(self):
        self._bank_ack_time = None
        self._dback_amount = None
        self._dback_status = None
        self._est_bank_receipt_time = None
        self._has_deposit_back = None

    @property
    def bank_ack_time(self):
        return self._bank_ack_time

    @bank_ack_time.setter
    def bank_ack_time(self, value):
        self._bank_ack_time = value
    @property
    def dback_amount(self):
        return self._dback_amount

    @dback_amount.setter
    def dback_amount(self, value):
        self._dback_amount = value
    @property
    def dback_status(self):
        return self._dback_status

    @dback_status.setter
    def dback_status(self, value):
        self._dback_status = value
    @property
    def est_bank_receipt_time(self):
        return self._est_bank_receipt_time

    @est_bank_receipt_time.setter
    def est_bank_receipt_time(self, value):
        self._est_bank_receipt_time = value
    @property
    def has_deposit_back(self):
        return self._has_deposit_back

    @has_deposit_back.setter
    def has_deposit_back(self, value):
        self._has_deposit_back = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_ack_time:
            if hasattr(self.bank_ack_time, 'to_alipay_dict'):
                params['bank_ack_time'] = self.bank_ack_time.to_alipay_dict()
            else:
                params['bank_ack_time'] = self.bank_ack_time
        if self.dback_amount:
            if hasattr(self.dback_amount, 'to_alipay_dict'):
                params['dback_amount'] = self.dback_amount.to_alipay_dict()
            else:
                params['dback_amount'] = self.dback_amount
        if self.dback_status:
            if hasattr(self.dback_status, 'to_alipay_dict'):
                params['dback_status'] = self.dback_status.to_alipay_dict()
            else:
                params['dback_status'] = self.dback_status
        if self.est_bank_receipt_time:
            if hasattr(self.est_bank_receipt_time, 'to_alipay_dict'):
                params['est_bank_receipt_time'] = self.est_bank_receipt_time.to_alipay_dict()
            else:
                params['est_bank_receipt_time'] = self.est_bank_receipt_time
        if self.has_deposit_back:
            if hasattr(self.has_deposit_back, 'to_alipay_dict'):
                params['has_deposit_back'] = self.has_deposit_back.to_alipay_dict()
            else:
                params['has_deposit_back'] = self.has_deposit_back
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepositBackInfo()
        if 'bank_ack_time' in d:
            o.bank_ack_time = d['bank_ack_time']
        if 'dback_amount' in d:
            o.dback_amount = d['dback_amount']
        if 'dback_status' in d:
            o.dback_status = d['dback_status']
        if 'est_bank_receipt_time' in d:
            o.est_bank_receipt_time = d['est_bank_receipt_time']
        if 'has_deposit_back' in d:
            o.has_deposit_back = d['has_deposit_back']
        return o


