#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEnterpriseexctrlEmployertitleCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._address = None
        self._agreement_no = None
        self._bank_account = None
        self._bank_name = None
        self._enterprise_id = None
        self._tax_register_no = None
        self._telephone = None
        self._title_code = None
        self._title_name = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
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
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title_code(self):
        return self._title_code

    @title_code.setter
    def title_code(self, value):
        self._title_code = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
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
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.tax_register_no:
            if hasattr(self.tax_register_no, 'to_alipay_dict'):
                params['tax_register_no'] = self.tax_register_no.to_alipay_dict()
            else:
                params['tax_register_no'] = self.tax_register_no
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.title_code:
            if hasattr(self.title_code, 'to_alipay_dict'):
                params['title_code'] = self.title_code.to_alipay_dict()
            else:
                params['title_code'] = self.title_code
        if self.title_name:
            if hasattr(self.title_name, 'to_alipay_dict'):
                params['title_name'] = self.title_name.to_alipay_dict()
            else:
                params['title_name'] = self.title_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEnterpriseexctrlEmployertitleCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'address' in d:
            o.address = d['address']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'tax_register_no' in d:
            o.tax_register_no = d['tax_register_no']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'title_code' in d:
            o.title_code = d['title_code']
        if 'title_name' in d:
            o.title_name = d['title_name']
        return o


