#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanMoneyTypeAmt(object):

    def __init__(self):
        self._fee = None
        self._intr = None
        self._ovd_fine = None
        self._ovd_int = None
        self._ovd_int_pny = None
        self._ovd_prin = None
        self._ovd_prin_pny = None
        self._prin = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def intr(self):
        return self._intr

    @intr.setter
    def intr(self, value):
        self._intr = value
    @property
    def ovd_fine(self):
        return self._ovd_fine

    @ovd_fine.setter
    def ovd_fine(self, value):
        self._ovd_fine = value
    @property
    def ovd_int(self):
        return self._ovd_int

    @ovd_int.setter
    def ovd_int(self, value):
        self._ovd_int = value
    @property
    def ovd_int_pny(self):
        return self._ovd_int_pny

    @ovd_int_pny.setter
    def ovd_int_pny(self, value):
        self._ovd_int_pny = value
    @property
    def ovd_prin(self):
        return self._ovd_prin

    @ovd_prin.setter
    def ovd_prin(self, value):
        self._ovd_prin = value
    @property
    def ovd_prin_pny(self):
        return self._ovd_prin_pny

    @ovd_prin_pny.setter
    def ovd_prin_pny(self, value):
        self._ovd_prin_pny = value
    @property
    def prin(self):
        return self._prin

    @prin.setter
    def prin(self, value):
        self._prin = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.intr:
            if hasattr(self.intr, 'to_alipay_dict'):
                params['intr'] = self.intr.to_alipay_dict()
            else:
                params['intr'] = self.intr
        if self.ovd_fine:
            if hasattr(self.ovd_fine, 'to_alipay_dict'):
                params['ovd_fine'] = self.ovd_fine.to_alipay_dict()
            else:
                params['ovd_fine'] = self.ovd_fine
        if self.ovd_int:
            if hasattr(self.ovd_int, 'to_alipay_dict'):
                params['ovd_int'] = self.ovd_int.to_alipay_dict()
            else:
                params['ovd_int'] = self.ovd_int
        if self.ovd_int_pny:
            if hasattr(self.ovd_int_pny, 'to_alipay_dict'):
                params['ovd_int_pny'] = self.ovd_int_pny.to_alipay_dict()
            else:
                params['ovd_int_pny'] = self.ovd_int_pny
        if self.ovd_prin:
            if hasattr(self.ovd_prin, 'to_alipay_dict'):
                params['ovd_prin'] = self.ovd_prin.to_alipay_dict()
            else:
                params['ovd_prin'] = self.ovd_prin
        if self.ovd_prin_pny:
            if hasattr(self.ovd_prin_pny, 'to_alipay_dict'):
                params['ovd_prin_pny'] = self.ovd_prin_pny.to_alipay_dict()
            else:
                params['ovd_prin_pny'] = self.ovd_prin_pny
        if self.prin:
            if hasattr(self.prin, 'to_alipay_dict'):
                params['prin'] = self.prin.to_alipay_dict()
            else:
                params['prin'] = self.prin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanMoneyTypeAmt()
        if 'fee' in d:
            o.fee = d['fee']
        if 'intr' in d:
            o.intr = d['intr']
        if 'ovd_fine' in d:
            o.ovd_fine = d['ovd_fine']
        if 'ovd_int' in d:
            o.ovd_int = d['ovd_int']
        if 'ovd_int_pny' in d:
            o.ovd_int_pny = d['ovd_int_pny']
        if 'ovd_prin' in d:
            o.ovd_prin = d['ovd_prin']
        if 'ovd_prin_pny' in d:
            o.ovd_prin_pny = d['ovd_prin_pny']
        if 'prin' in d:
            o.prin = d['prin']
        return o


