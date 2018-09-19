#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenRequestBatchSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenRequestBatchSendResponse, self).__init__()
        self._response_body = None

    @property
    def response_body(self):
        return self._response_body

    @response_body.setter
    def response_body(self, value):
        self._response_body = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenRequestBatchSendResponse, self).parse_response_content(response_content)
        if 'response_body' in response:
            self.response_body = response['response_body']
