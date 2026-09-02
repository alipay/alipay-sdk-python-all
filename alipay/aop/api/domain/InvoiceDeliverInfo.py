#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceDeliverInfo(object):

    def __init__(self):
        self._client_email = None
        self._client_phone = None
        self._deliver_type = None
        self._electronic_invoice_account = None
        self._file_type = None
        self._tinyapp_phone = None

    @property
    def client_email(self):
        return self._client_email

    @client_email.setter
    def client_email(self, value):
        self._client_email = value
    @property
    def client_phone(self):
        return self._client_phone

    @client_phone.setter
    def client_phone(self, value):
        self._client_phone = value
    @property
    def deliver_type(self):
        return self._deliver_type

    @deliver_type.setter
    def deliver_type(self, value):
        self._deliver_type = value
    @property
    def electronic_invoice_account(self):
        return self._electronic_invoice_account

    @electronic_invoice_account.setter
    def electronic_invoice_account(self, value):
        self._electronic_invoice_account = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def tinyapp_phone(self):
        return self._tinyapp_phone

    @tinyapp_phone.setter
    def tinyapp_phone(self, value):
        self._tinyapp_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_email:
            if hasattr(self.client_email, 'to_alipay_dict'):
                params['client_email'] = self.client_email.to_alipay_dict()
            else:
                params['client_email'] = self.client_email
        if self.client_phone:
            if hasattr(self.client_phone, 'to_alipay_dict'):
                params['client_phone'] = self.client_phone.to_alipay_dict()
            else:
                params['client_phone'] = self.client_phone
        if self.deliver_type:
            if hasattr(self.deliver_type, 'to_alipay_dict'):
                params['deliver_type'] = self.deliver_type.to_alipay_dict()
            else:
                params['deliver_type'] = self.deliver_type
        if self.electronic_invoice_account:
            if hasattr(self.electronic_invoice_account, 'to_alipay_dict'):
                params['electronic_invoice_account'] = self.electronic_invoice_account.to_alipay_dict()
            else:
                params['electronic_invoice_account'] = self.electronic_invoice_account
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.tinyapp_phone:
            if hasattr(self.tinyapp_phone, 'to_alipay_dict'):
                params['tinyapp_phone'] = self.tinyapp_phone.to_alipay_dict()
            else:
                params['tinyapp_phone'] = self.tinyapp_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceDeliverInfo()
        if 'client_email' in d:
            o.client_email = d['client_email']
        if 'client_phone' in d:
            o.client_phone = d['client_phone']
        if 'deliver_type' in d:
            o.deliver_type = d['deliver_type']
        if 'electronic_invoice_account' in d:
            o.electronic_invoice_account = d['electronic_invoice_account']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'tinyapp_phone' in d:
            o.tinyapp_phone = d['tinyapp_phone']
        return o


