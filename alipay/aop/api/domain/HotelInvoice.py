#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelInvoice(object):

    def __init__(self):
        self._invoice_mode = None
        self._invoice_purpose = None
        self._invoice_type = None
        self._order_invoice = None
        self._postage_provider = None

    @property
    def invoice_mode(self):
        return self._invoice_mode

    @invoice_mode.setter
    def invoice_mode(self, value):
        self._invoice_mode = value
    @property
    def invoice_purpose(self):
        return self._invoice_purpose

    @invoice_purpose.setter
    def invoice_purpose(self, value):
        self._invoice_purpose = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        if isinstance(value, list):
            self._invoice_type = list()
            for i in value:
                self._invoice_type.append(i)
    @property
    def order_invoice(self):
        return self._order_invoice

    @order_invoice.setter
    def order_invoice(self, value):
        self._order_invoice = value
    @property
    def postage_provider(self):
        return self._postage_provider

    @postage_provider.setter
    def postage_provider(self, value):
        self._postage_provider = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_mode:
            if hasattr(self.invoice_mode, 'to_alipay_dict'):
                params['invoice_mode'] = self.invoice_mode.to_alipay_dict()
            else:
                params['invoice_mode'] = self.invoice_mode
        if self.invoice_purpose:
            if hasattr(self.invoice_purpose, 'to_alipay_dict'):
                params['invoice_purpose'] = self.invoice_purpose.to_alipay_dict()
            else:
                params['invoice_purpose'] = self.invoice_purpose
        if self.invoice_type:
            if isinstance(self.invoice_type, list):
                for i in range(0, len(self.invoice_type)):
                    element = self.invoice_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_type[i] = element.to_alipay_dict()
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.order_invoice:
            if hasattr(self.order_invoice, 'to_alipay_dict'):
                params['order_invoice'] = self.order_invoice.to_alipay_dict()
            else:
                params['order_invoice'] = self.order_invoice
        if self.postage_provider:
            if hasattr(self.postage_provider, 'to_alipay_dict'):
                params['postage_provider'] = self.postage_provider.to_alipay_dict()
            else:
                params['postage_provider'] = self.postage_provider
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelInvoice()
        if 'invoice_mode' in d:
            o.invoice_mode = d['invoice_mode']
        if 'invoice_purpose' in d:
            o.invoice_purpose = d['invoice_purpose']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'order_invoice' in d:
            o.order_invoice = d['order_invoice']
        if 'postage_provider' in d:
            o.postage_provider = d['postage_provider']
        return o


