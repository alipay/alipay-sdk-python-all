#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceCompanyInfo import InvoiceCompanyInfo


class AlipayEbppInvoiceCompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceCompanyQueryResponse, self).__init__()
        self._invoice_company = None
        self._partner_id = None
        self._register_id = None

    @property
    def invoice_company(self):
        return self._invoice_company

    @invoice_company.setter
    def invoice_company(self, value):
        if isinstance(value, InvoiceCompanyInfo):
            self._invoice_company = value
        else:
            self._invoice_company = InvoiceCompanyInfo.from_alipay_dict(value)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceCompanyQueryResponse, self).parse_response_content(response_content)
        if 'invoice_company' in response:
            self.invoice_company = response['invoice_company']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'register_id' in response:
            self.register_id = response['register_id']
