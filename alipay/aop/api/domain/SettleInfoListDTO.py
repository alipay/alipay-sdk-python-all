#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleInfoListDTO(object):

    def __init__(self):
        self._fail_reason = None
        self._separate_ledger_rate = None
        self._settle_amount = None
        self._settle_role = None
        self._settle_status = None
        self._settle_time = None
        self._trans_in = None
        self._trans_in_type = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def separate_ledger_rate(self):
        return self._separate_ledger_rate

    @separate_ledger_rate.setter
    def separate_ledger_rate(self, value):
        self._separate_ledger_rate = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_role(self):
        return self._settle_role

    @settle_role.setter
    def settle_role(self, value):
        self._settle_role = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.separate_ledger_rate:
            if hasattr(self.separate_ledger_rate, 'to_alipay_dict'):
                params['separate_ledger_rate'] = self.separate_ledger_rate.to_alipay_dict()
            else:
                params['separate_ledger_rate'] = self.separate_ledger_rate
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_role:
            if hasattr(self.settle_role, 'to_alipay_dict'):
                params['settle_role'] = self.settle_role.to_alipay_dict()
            else:
                params['settle_role'] = self.settle_role
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleInfoListDTO()
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'separate_ledger_rate' in d:
            o.separate_ledger_rate = d['separate_ledger_rate']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_role' in d:
            o.settle_role = d['settle_role']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        return o


