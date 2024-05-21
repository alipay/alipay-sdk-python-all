#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEmailAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEmailAccountQueryResponse, self).__init__()
        self._email_address = None

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEmailAccountQueryResponse, self).parse_response_content(response_content)
        if 'email_address' in response:
            self.email_address = response['email_address']
