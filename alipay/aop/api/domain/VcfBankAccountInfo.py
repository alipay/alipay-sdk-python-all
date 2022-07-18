#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcfBankAccountInfo(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._bank_name = None
        self._country = None
        self._recon_inst = None
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
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def recon_inst(self):
        return self._recon_inst

    @recon_inst.setter
    def recon_inst(self, value):
        self._recon_inst = value
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
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.recon_inst:
            if hasattr(self.recon_inst, 'to_alipay_dict'):
                params['recon_inst'] = self.recon_inst.to_alipay_dict()
            else:
                params['recon_inst'] = self.recon_inst
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
        o = VcfBankAccountInfo()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'country' in d:
            o.country = d['country']
        if 'recon_inst' in d:
            o.recon_inst = d['recon_inst']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        return o


