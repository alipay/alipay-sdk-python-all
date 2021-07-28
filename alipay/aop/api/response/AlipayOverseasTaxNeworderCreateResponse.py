#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxNeworderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxNeworderCreateResponse, self).__init__()
        self._doc_id = None
        self._tax_order_no = None

    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def tax_order_no(self):
        return self._tax_order_no

    @tax_order_no.setter
    def tax_order_no(self, value):
        self._tax_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxNeworderCreateResponse, self).parse_response_content(response_content)
        if 'doc_id' in response:
            self.doc_id = response['doc_id']
        if 'tax_order_no' in response:
            self.tax_order_no = response['tax_order_no']
