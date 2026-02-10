#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NatrualPersonInvoiceAmountMonthly import NatrualPersonInvoiceAmountMonthly


class AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse, self).__init__()
        self._invoice_amount_list = None

    @property
    def invoice_amount_list(self):
        return self._invoice_amount_list

    @invoice_amount_list.setter
    def invoice_amount_list(self, value):
        if isinstance(value, list):
            self._invoice_amount_list = list()
            for i in value:
                if isinstance(i, NatrualPersonInvoiceAmountMonthly):
                    self._invoice_amount_list.append(i)
                else:
                    self._invoice_amount_list.append(NatrualPersonInvoiceAmountMonthly.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse, self).parse_response_content(response_content)
        if 'invoice_amount_list' in response:
            self.invoice_amount_list = response['invoice_amount_list']
