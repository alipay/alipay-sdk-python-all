#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceProductInfo import InvoiceProductInfo


class AlipayCommerceEcInvoiceProductQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcInvoiceProductQueryResponse, self).__init__()
        self._invoice_product_list = None

    @property
    def invoice_product_list(self):
        return self._invoice_product_list

    @invoice_product_list.setter
    def invoice_product_list(self, value):
        if isinstance(value, list):
            self._invoice_product_list = list()
            for i in value:
                if isinstance(i, InvoiceProductInfo):
                    self._invoice_product_list.append(i)
                else:
                    self._invoice_product_list.append(InvoiceProductInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcInvoiceProductQueryResponse, self).parse_response_content(response_content)
        if 'invoice_product_list' in response:
            self.invoice_product_list = response['invoice_product_list']
