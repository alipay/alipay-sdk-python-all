#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgTaxInfoOpenApiDto(object):

    def __init__(self):
        self._account_no = None
        self._address = None
        self._bank_name = None
        self._effect_date = None
        self._has_elec_account = None
        self._is_online_verify = None
        self._is_scan = None
        self._org_code = None
        self._org_id = None
        self._phone_no = None
        self._rates = None
        self._tax_no = None
        self._title = None
        self._type = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def has_elec_account(self):
        return self._has_elec_account

    @has_elec_account.setter
    def has_elec_account(self, value):
        self._has_elec_account = value
    @property
    def is_online_verify(self):
        return self._is_online_verify

    @is_online_verify.setter
    def is_online_verify(self, value):
        self._is_online_verify = value
    @property
    def is_scan(self):
        return self._is_scan

    @is_scan.setter
    def is_scan(self, value):
        self._is_scan = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self, value):
        if isinstance(value, list):
            self._rates = list()
            for i in value:
                self._rates.append(i)
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.has_elec_account:
            if hasattr(self.has_elec_account, 'to_alipay_dict'):
                params['has_elec_account'] = self.has_elec_account.to_alipay_dict()
            else:
                params['has_elec_account'] = self.has_elec_account
        if self.is_online_verify:
            if hasattr(self.is_online_verify, 'to_alipay_dict'):
                params['is_online_verify'] = self.is_online_verify.to_alipay_dict()
            else:
                params['is_online_verify'] = self.is_online_verify
        if self.is_scan:
            if hasattr(self.is_scan, 'to_alipay_dict'):
                params['is_scan'] = self.is_scan.to_alipay_dict()
            else:
                params['is_scan'] = self.is_scan
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.rates:
            if isinstance(self.rates, list):
                for i in range(0, len(self.rates)):
                    element = self.rates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rates[i] = element.to_alipay_dict()
            if hasattr(self.rates, 'to_alipay_dict'):
                params['rates'] = self.rates.to_alipay_dict()
            else:
                params['rates'] = self.rates
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgTaxInfoOpenApiDto()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'address' in d:
            o.address = d['address']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'has_elec_account' in d:
            o.has_elec_account = d['has_elec_account']
        if 'is_online_verify' in d:
            o.is_online_verify = d['is_online_verify']
        if 'is_scan' in d:
            o.is_scan = d['is_scan']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'rates' in d:
            o.rates = d['rates']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


