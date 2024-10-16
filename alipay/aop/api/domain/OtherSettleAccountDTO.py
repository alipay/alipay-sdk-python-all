#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OtherSettleAccountDTO(object):

    def __init__(self):
        self._payee_real_name = None
        self._separate_ledger_rate = None
        self._settle_account = None

    @property
    def payee_real_name(self):
        return self._payee_real_name

    @payee_real_name.setter
    def payee_real_name(self, value):
        self._payee_real_name = value
    @property
    def separate_ledger_rate(self):
        return self._separate_ledger_rate

    @separate_ledger_rate.setter
    def separate_ledger_rate(self, value):
        self._separate_ledger_rate = value
    @property
    def settle_account(self):
        return self._settle_account

    @settle_account.setter
    def settle_account(self, value):
        self._settle_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_real_name:
            if hasattr(self.payee_real_name, 'to_alipay_dict'):
                params['payee_real_name'] = self.payee_real_name.to_alipay_dict()
            else:
                params['payee_real_name'] = self.payee_real_name
        if self.separate_ledger_rate:
            if hasattr(self.separate_ledger_rate, 'to_alipay_dict'):
                params['separate_ledger_rate'] = self.separate_ledger_rate.to_alipay_dict()
            else:
                params['separate_ledger_rate'] = self.separate_ledger_rate
        if self.settle_account:
            if hasattr(self.settle_account, 'to_alipay_dict'):
                params['settle_account'] = self.settle_account.to_alipay_dict()
            else:
                params['settle_account'] = self.settle_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OtherSettleAccountDTO()
        if 'payee_real_name' in d:
            o.payee_real_name = d['payee_real_name']
        if 'separate_ledger_rate' in d:
            o.separate_ledger_rate = d['separate_ledger_rate']
        if 'settle_account' in d:
            o.settle_account = d['settle_account']
        return o


