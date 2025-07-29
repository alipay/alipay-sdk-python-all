#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeqiInvoiceClerk import LeqiInvoiceClerk


class AlipayCommerceEcInvoiceClerkQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcInvoiceClerkQueryResponse, self).__init__()
        self._invoice_clerk_list = None

    @property
    def invoice_clerk_list(self):
        return self._invoice_clerk_list

    @invoice_clerk_list.setter
    def invoice_clerk_list(self, value):
        if isinstance(value, list):
            self._invoice_clerk_list = list()
            for i in value:
                if isinstance(i, LeqiInvoiceClerk):
                    self._invoice_clerk_list.append(i)
                else:
                    self._invoice_clerk_list.append(LeqiInvoiceClerk.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcInvoiceClerkQueryResponse, self).parse_response_content(response_content)
        if 'invoice_clerk_list' in response:
            self.invoice_clerk_list = response['invoice_clerk_list']
