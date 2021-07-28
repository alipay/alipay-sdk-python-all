#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Invoice import Invoice
from alipay.aop.api.domain.WaybillInvoice import WaybillInvoice


class AlipayCommerceLogisticsInvoiceIstdwaybillCreateModel(object):

    def __init__(self):
        self._invoice = None
        self._logistics_code = None
        self._out_invoice_request_no = None
        self._waybill_invoices = None

    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        if isinstance(value, Invoice):
            self._invoice = value
        else:
            self._invoice = Invoice.from_alipay_dict(value)
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def out_invoice_request_no(self):
        return self._out_invoice_request_no

    @out_invoice_request_no.setter
    def out_invoice_request_no(self, value):
        self._out_invoice_request_no = value
    @property
    def waybill_invoices(self):
        return self._waybill_invoices

    @waybill_invoices.setter
    def waybill_invoices(self, value):
        if isinstance(value, list):
            self._waybill_invoices = list()
            for i in value:
                if isinstance(i, WaybillInvoice):
                    self._waybill_invoices.append(i)
                else:
                    self._waybill_invoices.append(WaybillInvoice.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.invoice:
            if hasattr(self.invoice, 'to_alipay_dict'):
                params['invoice'] = self.invoice.to_alipay_dict()
            else:
                params['invoice'] = self.invoice
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.out_invoice_request_no:
            if hasattr(self.out_invoice_request_no, 'to_alipay_dict'):
                params['out_invoice_request_no'] = self.out_invoice_request_no.to_alipay_dict()
            else:
                params['out_invoice_request_no'] = self.out_invoice_request_no
        if self.waybill_invoices:
            if isinstance(self.waybill_invoices, list):
                for i in range(0, len(self.waybill_invoices)):
                    element = self.waybill_invoices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.waybill_invoices[i] = element.to_alipay_dict()
            if hasattr(self.waybill_invoices, 'to_alipay_dict'):
                params['waybill_invoices'] = self.waybill_invoices.to_alipay_dict()
            else:
                params['waybill_invoices'] = self.waybill_invoices
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsInvoiceIstdwaybillCreateModel()
        if 'invoice' in d:
            o.invoice = d['invoice']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'out_invoice_request_no' in d:
            o.out_invoice_request_no = d['out_invoice_request_no']
        if 'waybill_invoices' in d:
            o.waybill_invoices = d['waybill_invoices']
        return o


