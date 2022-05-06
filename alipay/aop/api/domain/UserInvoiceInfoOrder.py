#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecipientInfoOrder import RecipientInfoOrder


class UserInvoiceInfoOrder(object):

    def __init__(self):
        self._address = None
        self._bank_account = None
        self._bank_name = None
        self._company_name = None
        self._ip_role_id = None
        self._recipient_info = None
        self._tax_no = None
        self._telephone = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
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
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def recipient_info(self):
        return self._recipient_info

    @recipient_info.setter
    def recipient_info(self, value):
        if isinstance(value, RecipientInfoOrder):
            self._recipient_info = value
        else:
            self._recipient_info = RecipientInfoOrder.from_alipay_dict(value)
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
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
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.recipient_info:
            if hasattr(self.recipient_info, 'to_alipay_dict'):
                params['recipient_info'] = self.recipient_info.to_alipay_dict()
            else:
                params['recipient_info'] = self.recipient_info
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInvoiceInfoOrder()
        if 'address' in d:
            o.address = d['address']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'recipient_info' in d:
            o.recipient_info = d['recipient_info']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'telephone' in d:
            o.telephone = d['telephone']
        return o


