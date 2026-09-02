#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasInvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasInvoiceApplyResponse, self).__init__()
        self._invoice_status = None
        self._saas_invoice_order_no = None

    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def saas_invoice_order_no(self):
        return self._saas_invoice_order_no

    @saas_invoice_order_no.setter
    def saas_invoice_order_no(self, value):
        self._saas_invoice_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasInvoiceApplyResponse, self).parse_response_content(response_content)
        if 'invoice_status' in response:
            self.invoice_status = response['invoice_status']
        if 'saas_invoice_order_no' in response:
            self.saas_invoice_order_no = response['saas_invoice_order_no']
