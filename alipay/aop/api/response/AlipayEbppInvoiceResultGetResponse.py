#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntInvoiceResult import AntInvoiceResult


class AlipayEbppInvoiceResultGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceResultGetResponse, self).__init__()
        self._invoice_result_list = None

    @property
    def invoice_result_list(self):
        return self._invoice_result_list

    @invoice_result_list.setter
    def invoice_result_list(self, value):
        if isinstance(value, list):
            self._invoice_result_list = list()
            for i in value:
                if isinstance(i, AntInvoiceResult):
                    self._invoice_result_list.append(i)
                else:
                    self._invoice_result_list.append(AntInvoiceResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceResultGetResponse, self).parse_response_content(response_content)
        if 'invoice_result_list' in response:
            self.invoice_result_list = response['invoice_result_list']
