#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceElementModel import InvoiceElementModel


class AlipayEbppInvoiceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceOrderQueryResponse, self).__init__()
        self._invoice_element_model = None
        self._order_no = None

    @property
    def invoice_element_model(self):
        return self._invoice_element_model

    @invoice_element_model.setter
    def invoice_element_model(self, value):
        if isinstance(value, InvoiceElementModel):
            self._invoice_element_model = value
        else:
            self._invoice_element_model = InvoiceElementModel.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceOrderQueryResponse, self).parse_response_content(response_content)
        if 'invoice_element_model' in response:
            self.invoice_element_model = response['invoice_element_model']
        if 'order_no' in response:
            self.order_no = response['order_no']
