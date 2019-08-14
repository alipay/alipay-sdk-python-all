#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportMessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportMessageSendResponse, self).__init__()
        self._error_code = None
        self._error_message = None
        self._failed_user_ids = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def failed_user_ids(self):
        return self._failed_user_ids

    @failed_user_ids.setter
    def failed_user_ids(self, value):
        self._failed_user_ids = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportMessageSendResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'failed_user_ids' in response:
            self.failed_user_ids = response['failed_user_ids']
