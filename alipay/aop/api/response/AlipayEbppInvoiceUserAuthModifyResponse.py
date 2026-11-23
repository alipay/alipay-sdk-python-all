#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceUserAuthModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceUserAuthModifyResponse, self).__init__()
        self._protocol_url = None

    @property
    def protocol_url(self):
        return self._protocol_url

    @protocol_url.setter
    def protocol_url(self, value):
        self._protocol_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceUserAuthModifyResponse, self).parse_response_content(response_content)
        if 'protocol_url' in response:
            self.protocol_url = response['protocol_url']
