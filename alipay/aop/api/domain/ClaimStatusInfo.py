#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimStatusInfo(object):

    def __init__(self):
        self._claim_amount = None
        self._pay_account_name = None
        self._pay_time = None
        self._status = None

    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def pay_account_name(self):
        return self._pay_account_name

    @pay_account_name.setter
    def pay_account_name(self, value):
        self._pay_account_name = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.pay_account_name:
            if hasattr(self.pay_account_name, 'to_alipay_dict'):
                params['pay_account_name'] = self.pay_account_name.to_alipay_dict()
            else:
                params['pay_account_name'] = self.pay_account_name
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimStatusInfo()
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'pay_account_name' in d:
            o.pay_account_name = d['pay_account_name']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'status' in d:
            o.status = d['status']
        return o


