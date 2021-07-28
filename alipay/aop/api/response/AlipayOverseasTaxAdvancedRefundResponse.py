#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxAdvancedRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxAdvancedRefundResponse, self).__init__()
        self._tax_refund_no = None

    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxAdvancedRefundResponse, self).parse_response_content(response_content)
        if 'tax_refund_no' in response:
            self.tax_refund_no = response['tax_refund_no']
