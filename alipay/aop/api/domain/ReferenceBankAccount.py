#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReferenceBankAccount(object):

    def __init__(self):
        self._bank = None
        self._bank_account_name = None
        self._bank_account_no = None
        self._bank_code = None
        self._branch_name = None

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value
    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, value):
        self._bank_account_name = value
    @property
    def bank_account_no(self):
        return self._bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self._bank_account_no = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank:
            if hasattr(self.bank, 'to_alipay_dict'):
                params['bank'] = self.bank.to_alipay_dict()
            else:
                params['bank'] = self.bank
        if self.bank_account_name:
            if hasattr(self.bank_account_name, 'to_alipay_dict'):
                params['bank_account_name'] = self.bank_account_name.to_alipay_dict()
            else:
                params['bank_account_name'] = self.bank_account_name
        if self.bank_account_no:
            if hasattr(self.bank_account_no, 'to_alipay_dict'):
                params['bank_account_no'] = self.bank_account_no.to_alipay_dict()
            else:
                params['bank_account_no'] = self.bank_account_no
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReferenceBankAccount()
        if 'bank' in d:
            o.bank = d['bank']
        if 'bank_account_name' in d:
            o.bank_account_name = d['bank_account_name']
        if 'bank_account_no' in d:
            o.bank_account_no = d['bank_account_no']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        return o


