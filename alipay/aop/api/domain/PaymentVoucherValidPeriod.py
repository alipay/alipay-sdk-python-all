#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherValidPeriod(object):

    def __init__(self):
        self._type = None
        self._valid_begin_time = None
        self._valid_days_after_receive = None
        self._valid_end_time = None
        self._wait_days_after_receive = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def valid_begin_time(self):
        return self._valid_begin_time

    @valid_begin_time.setter
    def valid_begin_time(self, value):
        self._valid_begin_time = value
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
    @property
    def wait_days_after_receive(self):
        return self._wait_days_after_receive

    @wait_days_after_receive.setter
    def wait_days_after_receive(self, value):
        self._wait_days_after_receive = value


    def to_alipay_dict(self):
        params = dict()
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.valid_begin_time:
            if hasattr(self.valid_begin_time, 'to_alipay_dict'):
                params['valid_begin_time'] = self.valid_begin_time.to_alipay_dict()
            else:
                params['valid_begin_time'] = self.valid_begin_time
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
        if self.wait_days_after_receive:
            if hasattr(self.wait_days_after_receive, 'to_alipay_dict'):
                params['wait_days_after_receive'] = self.wait_days_after_receive.to_alipay_dict()
            else:
                params['wait_days_after_receive'] = self.wait_days_after_receive
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherValidPeriod()
        if 'type' in d:
            o.type = d['type']
        if 'valid_begin_time' in d:
            o.valid_begin_time = d['valid_begin_time']
        if 'valid_days_after_receive' in d:
            o.valid_days_after_receive = d['valid_days_after_receive']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'wait_days_after_receive' in d:
            o.wait_days_after_receive = d['wait_days_after_receive']
        return o


