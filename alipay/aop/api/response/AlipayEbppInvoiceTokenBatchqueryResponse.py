#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceElementModel import InvoiceElementModel


class AlipayEbppInvoiceTokenBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTokenBatchqueryResponse, self).__init__()
        self._invoice_element_list = None
        self._user_id = None

    @property
    def invoice_element_list(self):
        return self._invoice_element_list

    @invoice_element_list.setter
    def invoice_element_list(self, value):
        if isinstance(value, list):
            self._invoice_element_list = list()
            for i in value:
                if isinstance(i, InvoiceElementModel):
                    self._invoice_element_list.append(i)
                else:
                    self._invoice_element_list.append(InvoiceElementModel.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTokenBatchqueryResponse, self).parse_response_content(response_content)
        if 'invoice_element_list' in response:
            self.invoice_element_list = response['invoice_element_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
