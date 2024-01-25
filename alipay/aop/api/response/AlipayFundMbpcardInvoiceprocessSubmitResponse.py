#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceOutIndexInfo import InvoiceOutIndexInfo


class AlipayFundMbpcardInvoiceprocessSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardInvoiceprocessSubmitResponse, self).__init__()
        self._invoice_list = None
        self._process_id = None
        self._process_status = None

    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, list):
            self._invoice_list = list()
            for i in value:
                if isinstance(i, InvoiceOutIndexInfo):
                    self._invoice_list.append(i)
                else:
                    self._invoice_list.append(InvoiceOutIndexInfo.from_alipay_dict(i))
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardInvoiceprocessSubmitResponse, self).parse_response_content(response_content)
        if 'invoice_list' in response:
            self.invoice_list = response['invoice_list']
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'process_status' in response:
            self.process_status = response['process_status']
