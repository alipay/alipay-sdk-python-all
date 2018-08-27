#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxOrderPayResponse, self).__init__()
        self._tax_no = None

    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxOrderPayResponse, self).parse_response_content(response_content)
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
