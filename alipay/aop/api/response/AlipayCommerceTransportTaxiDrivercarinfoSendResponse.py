#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDrivercarinfoSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDrivercarinfoSendResponse, self).__init__()
        self._code = None
        self._message = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDrivercarinfoSendResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'message' in response:
            self.message = response['message']
