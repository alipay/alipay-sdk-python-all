#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmailInvoiceInfo import EmailInvoiceInfo


class AlipayEbppInvoiceEmailInvoiceinfoSendModel(object):

    def __init__(self):
        self._email_address = None
        self._email_invoice_info_list = None
        self._out_email_id = None

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def email_invoice_info_list(self):
        return self._email_invoice_info_list

    @email_invoice_info_list.setter
    def email_invoice_info_list(self, value):
        if isinstance(value, list):
            self._email_invoice_info_list = list()
            for i in value:
                if isinstance(i, EmailInvoiceInfo):
                    self._email_invoice_info_list.append(i)
                else:
                    self._email_invoice_info_list.append(EmailInvoiceInfo.from_alipay_dict(i))
    @property
    def out_email_id(self):
        return self._out_email_id

    @out_email_id.setter
    def out_email_id(self, value):
        self._out_email_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.email_invoice_info_list:
            if isinstance(self.email_invoice_info_list, list):
                for i in range(0, len(self.email_invoice_info_list)):
                    element = self.email_invoice_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.email_invoice_info_list[i] = element.to_alipay_dict()
            if hasattr(self.email_invoice_info_list, 'to_alipay_dict'):
                params['email_invoice_info_list'] = self.email_invoice_info_list.to_alipay_dict()
            else:
                params['email_invoice_info_list'] = self.email_invoice_info_list
        if self.out_email_id:
            if hasattr(self.out_email_id, 'to_alipay_dict'):
                params['out_email_id'] = self.out_email_id.to_alipay_dict()
            else:
                params['out_email_id'] = self.out_email_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEmailInvoiceinfoSendModel()
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'email_invoice_info_list' in d:
            o.email_invoice_info_list = d['email_invoice_info_list']
        if 'out_email_id' in d:
            o.out_email_id = d['out_email_id']
        return o


