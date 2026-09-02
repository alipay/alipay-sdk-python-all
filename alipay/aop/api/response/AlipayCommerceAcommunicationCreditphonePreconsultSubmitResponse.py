#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCreditphonePreconsultSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphonePreconsultSubmitResponse, self).__init__()
        self._request_no = None

    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphonePreconsultSubmitResponse, self).parse_response_content(response_content)
        if 'request_no' in response:
            self.request_no = response['request_no']
