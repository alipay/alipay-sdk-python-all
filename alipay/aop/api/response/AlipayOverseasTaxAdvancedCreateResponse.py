#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxAdvancedCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxAdvancedCreateResponse, self).__init__()
        self._order_str = None
        self._out_tax_refund_no = None
        self._tax_refund_no = None

    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value
    @property
    def out_tax_refund_no(self):
        return self._out_tax_refund_no

    @out_tax_refund_no.setter
    def out_tax_refund_no(self, value):
        self._out_tax_refund_no = value
    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxAdvancedCreateResponse, self).parse_response_content(response_content)
        if 'order_str' in response:
            self.order_str = response['order_str']
        if 'out_tax_refund_no' in response:
            self.out_tax_refund_no = response['out_tax_refund_no']
        if 'tax_refund_no' in response:
            self.tax_refund_no = response['tax_refund_no']
