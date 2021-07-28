#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinanceBankAccountInfo(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._bank_address = None
        self._bank_city = None
        self._bank_id = None
        self._bank_province = None
        self._branch_id = None
        self._branch_name = None
        self._currency = None
        self._swift_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def bank_address(self):
        return self._bank_address

    @bank_address.setter
    def bank_address(self, value):
        self._bank_address = value
    @property
    def bank_city(self):
        return self._bank_city

    @bank_city.setter
    def bank_city(self, value):
        self._bank_city = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_province(self):
        return self._bank_province

    @bank_province.setter
    def bank_province(self, value):
        self._bank_province = value
    @property
    def branch_id(self):
        return self._branch_id

    @branch_id.setter
    def branch_id(self, value):
        self._branch_id = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
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
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.bank_address:
            if hasattr(self.bank_address, 'to_alipay_dict'):
                params['bank_address'] = self.bank_address.to_alipay_dict()
            else:
                params['bank_address'] = self.bank_address
        if self.bank_city:
            if hasattr(self.bank_city, 'to_alipay_dict'):
                params['bank_city'] = self.bank_city.to_alipay_dict()
            else:
                params['bank_city'] = self.bank_city
        if self.bank_id:
            if hasattr(self.bank_id, 'to_alipay_dict'):
                params['bank_id'] = self.bank_id.to_alipay_dict()
            else:
                params['bank_id'] = self.bank_id
        if self.bank_province:
            if hasattr(self.bank_province, 'to_alipay_dict'):
                params['bank_province'] = self.bank_province.to_alipay_dict()
            else:
                params['bank_province'] = self.bank_province
        if self.branch_id:
            if hasattr(self.branch_id, 'to_alipay_dict'):
                params['branch_id'] = self.branch_id.to_alipay_dict()
            else:
                params['branch_id'] = self.branch_id
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
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
        o = FinanceBankAccountInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_address' in d:
            o.bank_address = d['bank_address']
        if 'bank_city' in d:
            o.bank_city = d['bank_city']
        if 'bank_id' in d:
            o.bank_id = d['bank_id']
        if 'bank_province' in d:
            o.bank_province = d['bank_province']
        if 'branch_id' in d:
            o.branch_id = d['branch_id']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'currency' in d:
            o.currency = d['currency']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        return o


