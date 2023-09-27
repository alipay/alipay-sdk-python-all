#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankOrderInfo(object):

    def __init__(self):
        self._bank_serial_no = None
        self._capital_serial_no = None

    @property
    def bank_serial_no(self):
        return self._bank_serial_no

    @bank_serial_no.setter
    def bank_serial_no(self, value):
        self._bank_serial_no = value
    @property
    def capital_serial_no(self):
        return self._capital_serial_no

    @capital_serial_no.setter
    def capital_serial_no(self, value):
        self._capital_serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_serial_no:
            if hasattr(self.bank_serial_no, 'to_alipay_dict'):
                params['bank_serial_no'] = self.bank_serial_no.to_alipay_dict()
            else:
                params['bank_serial_no'] = self.bank_serial_no
        if self.capital_serial_no:
            if hasattr(self.capital_serial_no, 'to_alipay_dict'):
                params['capital_serial_no'] = self.capital_serial_no.to_alipay_dict()
            else:
                params['capital_serial_no'] = self.capital_serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankOrderInfo()
        if 'bank_serial_no' in d:
            o.bank_serial_no = d['bank_serial_no']
        if 'capital_serial_no' in d:
            o.capital_serial_no = d['capital_serial_no']
        return o


