#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObcInvoiceIssuerRequest(object):

    def __init__(self):
        self._bank_account = None
        self._bank_name = None
        self._emails = None
        self._invoice_title = None
        self._invoice_type = None
        self._post_code = None
        self._registered_address = None
        self._registered_phone_no = None
        self._source_uid = None
        self._tax_no = None

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
    def emails(self):
        return self._emails

    @emails.setter
    def emails(self, value):
        if isinstance(value, list):
            self._emails = list()
            for i in value:
                self._emails.append(i)
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        self._invoice_title = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, value):
        self._post_code = value
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
    def source_uid(self):
        return self._source_uid

    @source_uid.setter
    def source_uid(self, value):
        self._source_uid = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


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
        if self.emails:
            if isinstance(self.emails, list):
                for i in range(0, len(self.emails)):
                    element = self.emails[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.emails[i] = element.to_alipay_dict()
            if hasattr(self.emails, 'to_alipay_dict'):
                params['emails'] = self.emails.to_alipay_dict()
            else:
                params['emails'] = self.emails
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.post_code:
            if hasattr(self.post_code, 'to_alipay_dict'):
                params['post_code'] = self.post_code.to_alipay_dict()
            else:
                params['post_code'] = self.post_code
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
        if self.source_uid:
            if hasattr(self.source_uid, 'to_alipay_dict'):
                params['source_uid'] = self.source_uid.to_alipay_dict()
            else:
                params['source_uid'] = self.source_uid
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObcInvoiceIssuerRequest()
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'emails' in d:
            o.emails = d['emails']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'post_code' in d:
            o.post_code = d['post_code']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_phone_no' in d:
            o.registered_phone_no = d['registered_phone_no']
        if 'source_uid' in d:
            o.source_uid = d['source_uid']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


