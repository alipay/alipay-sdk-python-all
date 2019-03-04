#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfoKt import AddressInfoKt


class MerchantInvoiceInfoKt(object):

    def __init__(self):
        self._accept_electronic = None
        self._address = None
        self._auto_invoice = None
        self._bank_account = None
        self._bank_name = None
        self._mail_address = None
        self._mail_name = None
        self._mail_telephone = None
        self._tax_no = None
        self._tax_payer_qualification = None
        self._tax_payer_valid = None
        self._telephone = None
        self._title = None

    @property
    def accept_electronic(self):
        return self._accept_electronic

    @accept_electronic.setter
    def accept_electronic(self, value):
        self._accept_electronic = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def auto_invoice(self):
        return self._auto_invoice

    @auto_invoice.setter
    def auto_invoice(self, value):
        self._auto_invoice = value
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
    def mail_address(self):
        return self._mail_address

    @mail_address.setter
    def mail_address(self, value):
        if isinstance(value, AddressInfoKt):
            self._mail_address = value
        else:
            self._mail_address = AddressInfoKt.from_alipay_dict(value)
    @property
    def mail_name(self):
        return self._mail_name

    @mail_name.setter
    def mail_name(self, value):
        self._mail_name = value
    @property
    def mail_telephone(self):
        return self._mail_telephone

    @mail_telephone.setter
    def mail_telephone(self, value):
        self._mail_telephone = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def tax_payer_qualification(self):
        return self._tax_payer_qualification

    @tax_payer_qualification.setter
    def tax_payer_qualification(self, value):
        self._tax_payer_qualification = value
    @property
    def tax_payer_valid(self):
        return self._tax_payer_valid

    @tax_payer_valid.setter
    def tax_payer_valid(self, value):
        self._tax_payer_valid = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_electronic:
            if hasattr(self.accept_electronic, 'to_alipay_dict'):
                params['accept_electronic'] = self.accept_electronic.to_alipay_dict()
            else:
                params['accept_electronic'] = self.accept_electronic
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.auto_invoice:
            if hasattr(self.auto_invoice, 'to_alipay_dict'):
                params['auto_invoice'] = self.auto_invoice.to_alipay_dict()
            else:
                params['auto_invoice'] = self.auto_invoice
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
        if self.mail_address:
            if hasattr(self.mail_address, 'to_alipay_dict'):
                params['mail_address'] = self.mail_address.to_alipay_dict()
            else:
                params['mail_address'] = self.mail_address
        if self.mail_name:
            if hasattr(self.mail_name, 'to_alipay_dict'):
                params['mail_name'] = self.mail_name.to_alipay_dict()
            else:
                params['mail_name'] = self.mail_name
        if self.mail_telephone:
            if hasattr(self.mail_telephone, 'to_alipay_dict'):
                params['mail_telephone'] = self.mail_telephone.to_alipay_dict()
            else:
                params['mail_telephone'] = self.mail_telephone
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.tax_payer_qualification:
            if hasattr(self.tax_payer_qualification, 'to_alipay_dict'):
                params['tax_payer_qualification'] = self.tax_payer_qualification.to_alipay_dict()
            else:
                params['tax_payer_qualification'] = self.tax_payer_qualification
        if self.tax_payer_valid:
            if hasattr(self.tax_payer_valid, 'to_alipay_dict'):
                params['tax_payer_valid'] = self.tax_payer_valid.to_alipay_dict()
            else:
                params['tax_payer_valid'] = self.tax_payer_valid
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantInvoiceInfoKt()
        if 'accept_electronic' in d:
            o.accept_electronic = d['accept_electronic']
        if 'address' in d:
            o.address = d['address']
        if 'auto_invoice' in d:
            o.auto_invoice = d['auto_invoice']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'mail_address' in d:
            o.mail_address = d['mail_address']
        if 'mail_name' in d:
            o.mail_name = d['mail_name']
        if 'mail_telephone' in d:
            o.mail_telephone = d['mail_telephone']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'tax_payer_qualification' in d:
            o.tax_payer_qualification = d['tax_payer_qualification']
        if 'tax_payer_valid' in d:
            o.tax_payer_valid = d['tax_payer_valid']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'title' in d:
            o.title = d['title']
        return o


