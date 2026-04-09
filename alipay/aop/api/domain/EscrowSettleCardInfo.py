#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EscrowSettleCardInfo(object):

    def __init__(self):
        self._account_name = None
        self._bank_code = None
        self._bank_name = None
        self._branch_address = None
        self._branch_name = None
        self._card_no = None
        self._card_type = None
        self._pbc_bank_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def branch_address(self):
        return self._branch_address

    @branch_address.setter
    def branch_address(self, value):
        self._branch_address = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def pbc_bank_code(self):
        return self._pbc_bank_code

    @pbc_bank_code.setter
    def pbc_bank_code(self, value):
        self._pbc_bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.branch_address:
            if hasattr(self.branch_address, 'to_alipay_dict'):
                params['branch_address'] = self.branch_address.to_alipay_dict()
            else:
                params['branch_address'] = self.branch_address
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.pbc_bank_code:
            if hasattr(self.pbc_bank_code, 'to_alipay_dict'):
                params['pbc_bank_code'] = self.pbc_bank_code.to_alipay_dict()
            else:
                params['pbc_bank_code'] = self.pbc_bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EscrowSettleCardInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'branch_address' in d:
            o.branch_address = d['branch_address']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'pbc_bank_code' in d:
            o.pbc_bank_code = d['pbc_bank_code']
        return o


