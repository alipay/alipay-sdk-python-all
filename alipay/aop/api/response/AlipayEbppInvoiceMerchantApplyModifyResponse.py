#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantInvoiceUKDTO import MerchantInvoiceUKDTO


class AlipayEbppInvoiceMerchantApplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceMerchantApplyModifyResponse, self).__init__()
        self._error_invoices = None

    @property
    def error_invoices(self):
        return self._error_invoices

    @error_invoices.setter
    def error_invoices(self, value):
        if isinstance(value, list):
            self._error_invoices = list()
            for i in value:
                if isinstance(i, MerchantInvoiceUKDTO):
                    self._error_invoices.append(i)
                else:
                    self._error_invoices.append(MerchantInvoiceUKDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceMerchantApplyModifyResponse, self).parse_response_content(response_content)
        if 'error_invoices' in response:
            self.error_invoices = response['error_invoices']
