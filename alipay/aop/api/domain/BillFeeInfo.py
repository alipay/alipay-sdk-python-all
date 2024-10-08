#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillFeeInfo(object):

    def __init__(self):
        self._commission_cash = None
        self._commission_pid = None
        self._commission_pid_name = None
        self._commission_rate = None
        self._commission_refund_cash = None
        self._commission_refund_time = None
        self._commission_time = None
        self._commission_type = None

    @property
    def commission_cash(self):
        return self._commission_cash

    @commission_cash.setter
    def commission_cash(self, value):
        self._commission_cash = value
    @property
    def commission_pid(self):
        return self._commission_pid

    @commission_pid.setter
    def commission_pid(self, value):
        self._commission_pid = value
    @property
    def commission_pid_name(self):
        return self._commission_pid_name

    @commission_pid_name.setter
    def commission_pid_name(self, value):
        self._commission_pid_name = value
    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        self._commission_rate = value
    @property
    def commission_refund_cash(self):
        return self._commission_refund_cash

    @commission_refund_cash.setter
    def commission_refund_cash(self, value):
        self._commission_refund_cash = value
    @property
    def commission_refund_time(self):
        return self._commission_refund_time

    @commission_refund_time.setter
    def commission_refund_time(self, value):
        self._commission_refund_time = value
    @property
    def commission_time(self):
        return self._commission_time

    @commission_time.setter
    def commission_time(self, value):
        self._commission_time = value
    @property
    def commission_type(self):
        return self._commission_type

    @commission_type.setter
    def commission_type(self, value):
        self._commission_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_cash:
            if hasattr(self.commission_cash, 'to_alipay_dict'):
                params['commission_cash'] = self.commission_cash.to_alipay_dict()
            else:
                params['commission_cash'] = self.commission_cash
        if self.commission_pid:
            if hasattr(self.commission_pid, 'to_alipay_dict'):
                params['commission_pid'] = self.commission_pid.to_alipay_dict()
            else:
                params['commission_pid'] = self.commission_pid
        if self.commission_pid_name:
            if hasattr(self.commission_pid_name, 'to_alipay_dict'):
                params['commission_pid_name'] = self.commission_pid_name.to_alipay_dict()
            else:
                params['commission_pid_name'] = self.commission_pid_name
        if self.commission_rate:
            if hasattr(self.commission_rate, 'to_alipay_dict'):
                params['commission_rate'] = self.commission_rate.to_alipay_dict()
            else:
                params['commission_rate'] = self.commission_rate
        if self.commission_refund_cash:
            if hasattr(self.commission_refund_cash, 'to_alipay_dict'):
                params['commission_refund_cash'] = self.commission_refund_cash.to_alipay_dict()
            else:
                params['commission_refund_cash'] = self.commission_refund_cash
        if self.commission_refund_time:
            if hasattr(self.commission_refund_time, 'to_alipay_dict'):
                params['commission_refund_time'] = self.commission_refund_time.to_alipay_dict()
            else:
                params['commission_refund_time'] = self.commission_refund_time
        if self.commission_time:
            if hasattr(self.commission_time, 'to_alipay_dict'):
                params['commission_time'] = self.commission_time.to_alipay_dict()
            else:
                params['commission_time'] = self.commission_time
        if self.commission_type:
            if hasattr(self.commission_type, 'to_alipay_dict'):
                params['commission_type'] = self.commission_type.to_alipay_dict()
            else:
                params['commission_type'] = self.commission_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillFeeInfo()
        if 'commission_cash' in d:
            o.commission_cash = d['commission_cash']
        if 'commission_pid' in d:
            o.commission_pid = d['commission_pid']
        if 'commission_pid_name' in d:
            o.commission_pid_name = d['commission_pid_name']
        if 'commission_rate' in d:
            o.commission_rate = d['commission_rate']
        if 'commission_refund_cash' in d:
            o.commission_refund_cash = d['commission_refund_cash']
        if 'commission_refund_time' in d:
            o.commission_refund_time = d['commission_refund_time']
        if 'commission_time' in d:
            o.commission_time = d['commission_time']
        if 'commission_type' in d:
            o.commission_type = d['commission_type']
        return o


