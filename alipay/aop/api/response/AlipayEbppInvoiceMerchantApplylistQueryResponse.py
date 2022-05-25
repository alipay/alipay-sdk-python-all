#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceApplyDTO import InvoiceApplyDTO


class AlipayEbppInvoiceMerchantApplylistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceMerchantApplylistQueryResponse, self).__init__()
        self._invoice_apply_list = None

    @property
    def invoice_apply_list(self):
        return self._invoice_apply_list

    @invoice_apply_list.setter
    def invoice_apply_list(self, value):
        if isinstance(value, list):
            self._invoice_apply_list = list()
            for i in value:
                if isinstance(i, InvoiceApplyDTO):
                    self._invoice_apply_list.append(i)
                else:
                    self._invoice_apply_list.append(InvoiceApplyDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceMerchantApplylistQueryResponse, self).parse_response_content(response_content)
        if 'invoice_apply_list' in response:
            self.invoice_apply_list = response['invoice_apply_list']
