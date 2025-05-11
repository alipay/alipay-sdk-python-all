#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderInvoice(object):

    def __init__(self):
        self._img_file_url = None
        self._invoice_amount_without_tax = None
        self._invoice_no = None
        self._invoice_status = None
        self._invoice_status_message = None
        self._invoice_tax_amount = None
        self._invoice_type = None
        self._pdf_file_url = None

    @property
    def img_file_url(self):
        return self._img_file_url

    @img_file_url.setter
    def img_file_url(self, value):
        self._img_file_url = value
    @property
    def invoice_amount_without_tax(self):
        return self._invoice_amount_without_tax

    @invoice_amount_without_tax.setter
    def invoice_amount_without_tax(self, value):
        self._invoice_amount_without_tax = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_status_message(self):
        return self._invoice_status_message

    @invoice_status_message.setter
    def invoice_status_message(self, value):
        self._invoice_status_message = value
    @property
    def invoice_tax_amount(self):
        return self._invoice_tax_amount

    @invoice_tax_amount.setter
    def invoice_tax_amount(self, value):
        self._invoice_tax_amount = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def pdf_file_url(self):
        return self._pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, value):
        self._pdf_file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_file_url:
            if hasattr(self.img_file_url, 'to_alipay_dict'):
                params['img_file_url'] = self.img_file_url.to_alipay_dict()
            else:
                params['img_file_url'] = self.img_file_url
        if self.invoice_amount_without_tax:
            if hasattr(self.invoice_amount_without_tax, 'to_alipay_dict'):
                params['invoice_amount_without_tax'] = self.invoice_amount_without_tax.to_alipay_dict()
            else:
                params['invoice_amount_without_tax'] = self.invoice_amount_without_tax
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_status_message:
            if hasattr(self.invoice_status_message, 'to_alipay_dict'):
                params['invoice_status_message'] = self.invoice_status_message.to_alipay_dict()
            else:
                params['invoice_status_message'] = self.invoice_status_message
        if self.invoice_tax_amount:
            if hasattr(self.invoice_tax_amount, 'to_alipay_dict'):
                params['invoice_tax_amount'] = self.invoice_tax_amount.to_alipay_dict()
            else:
                params['invoice_tax_amount'] = self.invoice_tax_amount
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.pdf_file_url:
            if hasattr(self.pdf_file_url, 'to_alipay_dict'):
                params['pdf_file_url'] = self.pdf_file_url.to_alipay_dict()
            else:
                params['pdf_file_url'] = self.pdf_file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderInvoice()
        if 'img_file_url' in d:
            o.img_file_url = d['img_file_url']
        if 'invoice_amount_without_tax' in d:
            o.invoice_amount_without_tax = d['invoice_amount_without_tax']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_status_message' in d:
            o.invoice_status_message = d['invoice_status_message']
        if 'invoice_tax_amount' in d:
            o.invoice_tax_amount = d['invoice_tax_amount']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'pdf_file_url' in d:
            o.pdf_file_url = d['pdf_file_url']
        return o


