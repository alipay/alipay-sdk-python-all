#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionOrderOnceInfo(object):

    def __init__(self):
        self._certificate_serial = None
        self._deduction_amount = None
        self._deduction_cash = None
        self._period = None

    @property
    def certificate_serial(self):
        return self._certificate_serial

    @certificate_serial.setter
    def certificate_serial(self, value):
        self._certificate_serial = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_cash(self):
        return self._deduction_cash

    @deduction_cash.setter
    def deduction_cash(self, value):
        self._deduction_cash = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_serial:
            if hasattr(self.certificate_serial, 'to_alipay_dict'):
                params['certificate_serial'] = self.certificate_serial.to_alipay_dict()
            else:
                params['certificate_serial'] = self.certificate_serial
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_cash:
            if hasattr(self.deduction_cash, 'to_alipay_dict'):
                params['deduction_cash'] = self.deduction_cash.to_alipay_dict()
            else:
                params['deduction_cash'] = self.deduction_cash
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionOrderOnceInfo()
        if 'certificate_serial' in d:
            o.certificate_serial = d['certificate_serial']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_cash' in d:
            o.deduction_cash = d['deduction_cash']
        if 'period' in d:
            o.period = d['period']
        return o


