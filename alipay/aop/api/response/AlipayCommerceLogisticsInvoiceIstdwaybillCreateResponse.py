#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WaybillInvoiceIstd import WaybillInvoiceIstd


class AlipayCommerceLogisticsInvoiceIstdwaybillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsInvoiceIstdwaybillCreateResponse, self).__init__()
        self._invoice_fee = None
        self._status = None
        self._waybill_invoices = None

    @property
    def invoice_fee(self):
        return self._invoice_fee

    @invoice_fee.setter
    def invoice_fee(self, value):
        self._invoice_fee = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def waybill_invoices(self):
        return self._waybill_invoices

    @waybill_invoices.setter
    def waybill_invoices(self, value):
        if isinstance(value, list):
            self._waybill_invoices = list()
            for i in value:
                if isinstance(i, WaybillInvoiceIstd):
                    self._waybill_invoices.append(i)
                else:
                    self._waybill_invoices.append(WaybillInvoiceIstd.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsInvoiceIstdwaybillCreateResponse, self).parse_response_content(response_content)
        if 'invoice_fee' in response:
            self.invoice_fee = response['invoice_fee']
        if 'status' in response:
            self.status = response['status']
        if 'waybill_invoices' in response:
            self.waybill_invoices = response['waybill_invoices']
