#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotSdarttoolPrintSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSdarttoolPrintSendResponse, self).__init__()
        self._print_no = None

    @property
    def print_no(self):
        return self._print_no

    @print_no.setter
    def print_no(self, value):
        self._print_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSdarttoolPrintSendResponse, self).parse_response_content(response_content)
        if 'print_no' in response:
            self.print_no = response['print_no']
