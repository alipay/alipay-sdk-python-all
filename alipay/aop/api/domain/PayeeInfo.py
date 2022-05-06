#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayeeInfo(object):

    def __init__(self):
        self._payee_account_name = None
        self._payee_account_no = None
        self._payee_bank_code = None

    @property
    def payee_account_name(self):
        return self._payee_account_name

    @payee_account_name.setter
    def payee_account_name(self, value):
        self._payee_account_name = value
    @property
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_bank_code(self):
        return self._payee_bank_code

    @payee_bank_code.setter
    def payee_bank_code(self, value):
        self._payee_bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_account_name:
            if hasattr(self.payee_account_name, 'to_alipay_dict'):
                params['payee_account_name'] = self.payee_account_name.to_alipay_dict()
            else:
                params['payee_account_name'] = self.payee_account_name
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_bank_code:
            if hasattr(self.payee_bank_code, 'to_alipay_dict'):
                params['payee_bank_code'] = self.payee_bank_code.to_alipay_dict()
            else:
                params['payee_bank_code'] = self.payee_bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayeeInfo()
        if 'payee_account_name' in d:
            o.payee_account_name = d['payee_account_name']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_bank_code' in d:
            o.payee_bank_code = d['payee_bank_code']
        return o


