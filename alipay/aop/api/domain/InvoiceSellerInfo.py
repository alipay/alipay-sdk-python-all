#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceSellerInfo(object):

    def __init__(self):
        self._seller_address = None
        self._seller_bank = None
        self._seller_bank_account = None
        self._seller_name = None
        self._seller_phone = None
        self._seller_tax_no = None

    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank(self):
        return self._seller_bank

    @seller_bank.setter
    def seller_bank(self, value):
        self._seller_bank = value
    @property
    def seller_bank_account(self):
        return self._seller_bank_account

    @seller_bank_account.setter
    def seller_bank_account(self, value):
        self._seller_bank_account = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_phone(self):
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, value):
        self._seller_phone = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank:
            if hasattr(self.seller_bank, 'to_alipay_dict'):
                params['seller_bank'] = self.seller_bank.to_alipay_dict()
            else:
                params['seller_bank'] = self.seller_bank
        if self.seller_bank_account:
            if hasattr(self.seller_bank_account, 'to_alipay_dict'):
                params['seller_bank_account'] = self.seller_bank_account.to_alipay_dict()
            else:
                params['seller_bank_account'] = self.seller_bank_account
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_phone:
            if hasattr(self.seller_phone, 'to_alipay_dict'):
                params['seller_phone'] = self.seller_phone.to_alipay_dict()
            else:
                params['seller_phone'] = self.seller_phone
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceSellerInfo()
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank' in d:
            o.seller_bank = d['seller_bank']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_phone' in d:
            o.seller_phone = d['seller_phone']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        return o


