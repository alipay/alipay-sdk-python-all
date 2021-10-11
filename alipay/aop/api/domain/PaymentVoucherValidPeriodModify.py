#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherValidPeriodModify(object):

    def __init__(self):
        self._valid_days_after_receive = None
        self._valid_end_time = None

    @property
    def valid_days_after_receive(self):
        return self._valid_days_after_receive

    @valid_days_after_receive.setter
    def valid_days_after_receive(self, value):
        self._valid_days_after_receive = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.valid_days_after_receive:
            if hasattr(self.valid_days_after_receive, 'to_alipay_dict'):
                params['valid_days_after_receive'] = self.valid_days_after_receive.to_alipay_dict()
            else:
                params['valid_days_after_receive'] = self.valid_days_after_receive
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherValidPeriodModify()
        if 'valid_days_after_receive' in d:
            o.valid_days_after_receive = d['valid_days_after_receive']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        return o


