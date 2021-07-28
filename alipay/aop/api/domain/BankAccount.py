#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankAccount(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._bank_branch_code = None
        self._bank_branch_name = None
        self._bank_city_name = None
        self._bank_code = None
        self._bank_name = None
        self._bank_prov_name = None
        self._holder_cert_no = None
        self._holder_name = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def bank_branch_code(self):
        return self._bank_branch_code

    @bank_branch_code.setter
    def bank_branch_code(self, value):
        self._bank_branch_code = value
    @property
    def bank_branch_name(self):
        return self._bank_branch_name

    @bank_branch_name.setter
    def bank_branch_name(self, value):
        self._bank_branch_name = value
    @property
    def bank_city_name(self):
        return self._bank_city_name

    @bank_city_name.setter
    def bank_city_name(self, value):
        self._bank_city_name = value
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
    def bank_prov_name(self):
        return self._bank_prov_name

    @bank_prov_name.setter
    def bank_prov_name(self, value):
        self._bank_prov_name = value
    @property
    def holder_cert_no(self):
        return self._holder_cert_no

    @holder_cert_no.setter
    def holder_cert_no(self, value):
        self._holder_cert_no = value
    @property
    def holder_name(self):
        return self._holder_name

    @holder_name.setter
    def holder_name(self, value):
        self._holder_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.bank_branch_code:
            if hasattr(self.bank_branch_code, 'to_alipay_dict'):
                params['bank_branch_code'] = self.bank_branch_code.to_alipay_dict()
            else:
                params['bank_branch_code'] = self.bank_branch_code
        if self.bank_branch_name:
            if hasattr(self.bank_branch_name, 'to_alipay_dict'):
                params['bank_branch_name'] = self.bank_branch_name.to_alipay_dict()
            else:
                params['bank_branch_name'] = self.bank_branch_name
        if self.bank_city_name:
            if hasattr(self.bank_city_name, 'to_alipay_dict'):
                params['bank_city_name'] = self.bank_city_name.to_alipay_dict()
            else:
                params['bank_city_name'] = self.bank_city_name
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
        if self.bank_prov_name:
            if hasattr(self.bank_prov_name, 'to_alipay_dict'):
                params['bank_prov_name'] = self.bank_prov_name.to_alipay_dict()
            else:
                params['bank_prov_name'] = self.bank_prov_name
        if self.holder_cert_no:
            if hasattr(self.holder_cert_no, 'to_alipay_dict'):
                params['holder_cert_no'] = self.holder_cert_no.to_alipay_dict()
            else:
                params['holder_cert_no'] = self.holder_cert_no
        if self.holder_name:
            if hasattr(self.holder_name, 'to_alipay_dict'):
                params['holder_name'] = self.holder_name.to_alipay_dict()
            else:
                params['holder_name'] = self.holder_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankAccount()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_branch_code' in d:
            o.bank_branch_code = d['bank_branch_code']
        if 'bank_branch_name' in d:
            o.bank_branch_name = d['bank_branch_name']
        if 'bank_city_name' in d:
            o.bank_city_name = d['bank_city_name']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bank_prov_name' in d:
            o.bank_prov_name = d['bank_prov_name']
        if 'holder_cert_no' in d:
            o.holder_cert_no = d['holder_cert_no']
        if 'holder_name' in d:
            o.holder_name = d['holder_name']
        return o


