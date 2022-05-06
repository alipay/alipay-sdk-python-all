#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MonitorInfo(object):

    def __init__(self):
        self._monitor_account_name = None
        self._monitor_account_no = None
        self._monitor_bank_code = None

    @property
    def monitor_account_name(self):
        return self._monitor_account_name

    @monitor_account_name.setter
    def monitor_account_name(self, value):
        self._monitor_account_name = value
    @property
    def monitor_account_no(self):
        return self._monitor_account_no

    @monitor_account_no.setter
    def monitor_account_no(self, value):
        self._monitor_account_no = value
    @property
    def monitor_bank_code(self):
        return self._monitor_bank_code

    @monitor_bank_code.setter
    def monitor_bank_code(self, value):
        self._monitor_bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.monitor_account_name:
            if hasattr(self.monitor_account_name, 'to_alipay_dict'):
                params['monitor_account_name'] = self.monitor_account_name.to_alipay_dict()
            else:
                params['monitor_account_name'] = self.monitor_account_name
        if self.monitor_account_no:
            if hasattr(self.monitor_account_no, 'to_alipay_dict'):
                params['monitor_account_no'] = self.monitor_account_no.to_alipay_dict()
            else:
                params['monitor_account_no'] = self.monitor_account_no
        if self.monitor_bank_code:
            if hasattr(self.monitor_bank_code, 'to_alipay_dict'):
                params['monitor_bank_code'] = self.monitor_bank_code.to_alipay_dict()
            else:
                params['monitor_bank_code'] = self.monitor_bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MonitorInfo()
        if 'monitor_account_name' in d:
            o.monitor_account_name = d['monitor_account_name']
        if 'monitor_account_no' in d:
            o.monitor_account_no = d['monitor_account_no']
        if 'monitor_bank_code' in d:
            o.monitor_bank_code = d['monitor_bank_code']
        return o


