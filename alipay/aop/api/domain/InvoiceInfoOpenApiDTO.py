#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceInfoOpenApiDTO(object):

    def __init__(self):
        self._bank_account = None
        self._bank_name = None
        self._company_name = None
        self._ou_code = None
        self._registered_address = None
        self._registered_phone_no = None
        self._tax_no = None
        self._taxpayer_type = None

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registered_phone_no(self):
        return self._registered_phone_no

    @registered_phone_no.setter
    def registered_phone_no(self, value):
        self._registered_phone_no = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def taxpayer_type(self):
        return self._taxpayer_type

    @taxpayer_type.setter
    def taxpayer_type(self, value):
        self._taxpayer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.registered_phone_no:
            if hasattr(self.registered_phone_no, 'to_alipay_dict'):
                params['registered_phone_no'] = self.registered_phone_no.to_alipay_dict()
            else:
                params['registered_phone_no'] = self.registered_phone_no
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.taxpayer_type:
            if hasattr(self.taxpayer_type, 'to_alipay_dict'):
                params['taxpayer_type'] = self.taxpayer_type.to_alipay_dict()
            else:
                params['taxpayer_type'] = self.taxpayer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceInfoOpenApiDTO()
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_phone_no' in d:
            o.registered_phone_no = d['registered_phone_no']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'taxpayer_type' in d:
            o.taxpayer_type = d['taxpayer_type']
        return o


