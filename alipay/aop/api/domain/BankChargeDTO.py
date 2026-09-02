#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class BankChargeDTO(object):

    def __init__(self):
        self._bank_feecharge_amount = None
        self._bank_feecharge_selectable = None
        self._bank_feecharge_type = None

    @property
    def bank_feecharge_amount(self):
        return self._bank_feecharge_amount

    @bank_feecharge_amount.setter
    def bank_feecharge_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._bank_feecharge_amount = value
        else:
            self._bank_feecharge_amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def bank_feecharge_selectable(self):
        return self._bank_feecharge_selectable

    @bank_feecharge_selectable.setter
    def bank_feecharge_selectable(self, value):
        self._bank_feecharge_selectable = value
    @property
    def bank_feecharge_type(self):
        return self._bank_feecharge_type

    @bank_feecharge_type.setter
    def bank_feecharge_type(self, value):
        self._bank_feecharge_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_feecharge_amount:
            if hasattr(self.bank_feecharge_amount, 'to_alipay_dict'):
                params['bank_feecharge_amount'] = self.bank_feecharge_amount.to_alipay_dict()
            else:
                params['bank_feecharge_amount'] = self.bank_feecharge_amount
        if self.bank_feecharge_selectable:
            if hasattr(self.bank_feecharge_selectable, 'to_alipay_dict'):
                params['bank_feecharge_selectable'] = self.bank_feecharge_selectable.to_alipay_dict()
            else:
                params['bank_feecharge_selectable'] = self.bank_feecharge_selectable
        if self.bank_feecharge_type:
            if hasattr(self.bank_feecharge_type, 'to_alipay_dict'):
                params['bank_feecharge_type'] = self.bank_feecharge_type.to_alipay_dict()
            else:
                params['bank_feecharge_type'] = self.bank_feecharge_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankChargeDTO()
        if 'bank_feecharge_amount' in d:
            o.bank_feecharge_amount = d['bank_feecharge_amount']
        if 'bank_feecharge_selectable' in d:
            o.bank_feecharge_selectable = d['bank_feecharge_selectable']
        if 'bank_feecharge_type' in d:
            o.bank_feecharge_type = d['bank_feecharge_type']
        return o


