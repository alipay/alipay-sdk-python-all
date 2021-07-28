#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceRegisterCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceRegisterCreateResponse, self).__init__()
        self._register_id = None

    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceRegisterCreateResponse, self).parse_response_content(response_content)
        if 'register_id' in response:
            self.register_id = response['register_id']
