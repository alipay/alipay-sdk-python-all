#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstallmentValue import InstallmentValue


class LoanChargeInfo(object):

    def __init__(self):
        self._charge_code = None
        self._charge_name = None
        self._instal_chrg_rate = None

    @property
    def charge_code(self):
        return self._charge_code

    @charge_code.setter
    def charge_code(self, value):
        self._charge_code = value
    @property
    def charge_name(self):
        return self._charge_name

    @charge_name.setter
    def charge_name(self, value):
        self._charge_name = value
    @property
    def instal_chrg_rate(self):
        return self._instal_chrg_rate

    @instal_chrg_rate.setter
    def instal_chrg_rate(self, value):
        if isinstance(value, InstallmentValue):
            self._instal_chrg_rate = value
        else:
            self._instal_chrg_rate = InstallmentValue.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.charge_code:
            if hasattr(self.charge_code, 'to_alipay_dict'):
                params['charge_code'] = self.charge_code.to_alipay_dict()
            else:
                params['charge_code'] = self.charge_code
        if self.charge_name:
            if hasattr(self.charge_name, 'to_alipay_dict'):
                params['charge_name'] = self.charge_name.to_alipay_dict()
            else:
                params['charge_name'] = self.charge_name
        if self.instal_chrg_rate:
            if hasattr(self.instal_chrg_rate, 'to_alipay_dict'):
                params['instal_chrg_rate'] = self.instal_chrg_rate.to_alipay_dict()
            else:
                params['instal_chrg_rate'] = self.instal_chrg_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanChargeInfo()
        if 'charge_code' in d:
            o.charge_code = d['charge_code']
        if 'charge_name' in d:
            o.charge_name = d['charge_name']
        if 'instal_chrg_rate' in d:
            o.instal_chrg_rate = d['instal_chrg_rate']
        return o


