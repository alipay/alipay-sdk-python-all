#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiPaymentMethodOrder(object):

    def __init__(self):
        self._account_name = None
        self._account_number = None
        self._account_type = None
        self._bank_address = None
        self._bank_code = None
        self._bank_name = None
        self._bic = None
        self._branch_code = None
        self._branch_name = None
        self._cnaps_code = None
        self._currency = None
        self._iban = None
        self._main_bank_bame = None
        self._sub_bank_name = None
        self._swift_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def bank_address(self):
        return self._bank_address

    @bank_address.setter
    def bank_address(self, value):
        self._bank_address = value
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
    def bic(self):
        return self._bic

    @bic.setter
    def bic(self, value):
        self._bic = value
    @property
    def branch_code(self):
        return self._branch_code

    @branch_code.setter
    def branch_code(self, value):
        self._branch_code = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def cnaps_code(self):
        return self._cnaps_code

    @cnaps_code.setter
    def cnaps_code(self, value):
        self._cnaps_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def iban(self):
        return self._iban

    @iban.setter
    def iban(self, value):
        self._iban = value
    @property
    def main_bank_bame(self):
        return self._main_bank_bame

    @main_bank_bame.setter
    def main_bank_bame(self, value):
        self._main_bank_bame = value
    @property
    def sub_bank_name(self):
        return self._sub_bank_name

    @sub_bank_name.setter
    def sub_bank_name(self, value):
        self._sub_bank_name = value
    @property
    def swift_code(self):
        return self._swift_code

    @swift_code.setter
    def swift_code(self, value):
        self._swift_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_number:
            if hasattr(self.account_number, 'to_alipay_dict'):
                params['account_number'] = self.account_number.to_alipay_dict()
            else:
                params['account_number'] = self.account_number
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.bank_address:
            if hasattr(self.bank_address, 'to_alipay_dict'):
                params['bank_address'] = self.bank_address.to_alipay_dict()
            else:
                params['bank_address'] = self.bank_address
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
        if self.bic:
            if hasattr(self.bic, 'to_alipay_dict'):
                params['bic'] = self.bic.to_alipay_dict()
            else:
                params['bic'] = self.bic
        if self.branch_code:
            if hasattr(self.branch_code, 'to_alipay_dict'):
                params['branch_code'] = self.branch_code.to_alipay_dict()
            else:
                params['branch_code'] = self.branch_code
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.cnaps_code:
            if hasattr(self.cnaps_code, 'to_alipay_dict'):
                params['cnaps_code'] = self.cnaps_code.to_alipay_dict()
            else:
                params['cnaps_code'] = self.cnaps_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.iban:
            if hasattr(self.iban, 'to_alipay_dict'):
                params['iban'] = self.iban.to_alipay_dict()
            else:
                params['iban'] = self.iban
        if self.main_bank_bame:
            if hasattr(self.main_bank_bame, 'to_alipay_dict'):
                params['main_bank_bame'] = self.main_bank_bame.to_alipay_dict()
            else:
                params['main_bank_bame'] = self.main_bank_bame
        if self.sub_bank_name:
            if hasattr(self.sub_bank_name, 'to_alipay_dict'):
                params['sub_bank_name'] = self.sub_bank_name.to_alipay_dict()
            else:
                params['sub_bank_name'] = self.sub_bank_name
        if self.swift_code:
            if hasattr(self.swift_code, 'to_alipay_dict'):
                params['swift_code'] = self.swift_code.to_alipay_dict()
            else:
                params['swift_code'] = self.swift_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPaymentMethodOrder()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_number' in d:
            o.account_number = d['account_number']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_address' in d:
            o.bank_address = d['bank_address']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bic' in d:
            o.bic = d['bic']
        if 'branch_code' in d:
            o.branch_code = d['branch_code']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'cnaps_code' in d:
            o.cnaps_code = d['cnaps_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'iban' in d:
            o.iban = d['iban']
        if 'main_bank_bame' in d:
            o.main_bank_bame = d['main_bank_bame']
        if 'sub_bank_name' in d:
            o.sub_bank_name = d['sub_bank_name']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        return o


