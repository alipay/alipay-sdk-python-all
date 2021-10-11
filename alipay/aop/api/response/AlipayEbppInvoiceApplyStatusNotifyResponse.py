#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceUkDTO import InvoiceUkDTO


class AlipayEbppInvoiceApplyStatusNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceApplyStatusNotifyResponse, self).__init__()
        self._missing_invoices = None
        self._update_success = None

    @property
    def missing_invoices(self):
        return self._missing_invoices

    @missing_invoices.setter
    def missing_invoices(self, value):
        if isinstance(value, list):
            self._missing_invoices = list()
            for i in value:
                if isinstance(i, InvoiceUkDTO):
                    self._missing_invoices.append(i)
                else:
                    self._missing_invoices.append(InvoiceUkDTO.from_alipay_dict(i))
    @property
    def update_success(self):
        return self._update_success

    @update_success.setter
    def update_success(self, value):
        self._update_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceApplyStatusNotifyResponse, self).parse_response_content(response_content)
        if 'missing_invoices' in response:
            self.missing_invoices = response['missing_invoices']
        if 'update_success' in response:
            self.update_success = response['update_success']
