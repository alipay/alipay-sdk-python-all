#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Invoice(object):

    def __init__(self):
        self._email = None
        self._invoice_content = None
        self._invoice_fee = None
        self._invoice_title = None
        self._invoice_type = None
        self._phone = None
        self._receiver = None
        self._tax_number = None
        self._title_type = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def invoice_content(self):
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, value):
        self._invoice_content = value
    @property
    def invoice_fee(self):
        return self._invoice_fee

    @invoice_fee.setter
    def invoice_fee(self, value):
        self._invoice_fee = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def tax_number(self):
        return self._tax_number

    @tax_number.setter
    def tax_number(self, value):
        self._tax_number = value
    @property
    def title_type(self):
        return self._title_type

    @title_type.setter
    def title_type(self, value):
        self._title_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.invoice_content:
            if hasattr(self.invoice_content, 'to_alipay_dict'):
                params['invoice_content'] = self.invoice_content.to_alipay_dict()
            else:
                params['invoice_content'] = self.invoice_content
        if self.invoice_fee:
            if hasattr(self.invoice_fee, 'to_alipay_dict'):
                params['invoice_fee'] = self.invoice_fee.to_alipay_dict()
            else:
                params['invoice_fee'] = self.invoice_fee
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.tax_number:
            if hasattr(self.tax_number, 'to_alipay_dict'):
                params['tax_number'] = self.tax_number.to_alipay_dict()
            else:
                params['tax_number'] = self.tax_number
        if self.title_type:
            if hasattr(self.title_type, 'to_alipay_dict'):
                params['title_type'] = self.title_type.to_alipay_dict()
            else:
                params['title_type'] = self.title_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Invoice()
        if 'email' in d:
            o.email = d['email']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'invoice_fee' in d:
            o.invoice_fee = d['invoice_fee']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'tax_number' in d:
            o.tax_number = d['tax_number']
        if 'title_type' in d:
            o.title_type = d['title_type']
        return o


