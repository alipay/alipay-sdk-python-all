#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiTripinvoiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiTripinvoiceApplyResponse, self).__init__()
        self._img_file_url = None
        self._invoice_id = None
        self._pdf_file_url = None

    @property
    def img_file_url(self):
        return self._img_file_url

    @img_file_url.setter
    def img_file_url(self, value):
        self._img_file_url = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def pdf_file_url(self):
        return self._pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, value):
        self._pdf_file_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiTripinvoiceApplyResponse, self).parse_response_content(response_content)
        if 'img_file_url' in response:
            self.img_file_url = response['img_file_url']
        if 'invoice_id' in response:
            self.invoice_id = response['invoice_id']
        if 'pdf_file_url' in response:
            self.pdf_file_url = response['pdf_file_url']
