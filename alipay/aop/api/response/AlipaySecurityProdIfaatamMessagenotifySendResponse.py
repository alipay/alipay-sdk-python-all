#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdIfaatamMessagenotifySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdIfaatamMessagenotifySendResponse, self).__init__()
        self._return_code = None
        self._return_msg = None
        self._success = None

    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_msg(self):
        return self._return_msg

    @return_msg.setter
    def return_msg(self, value):
        self._return_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdIfaatamMessagenotifySendResponse, self).parse_response_content(response_content)
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_msg' in response:
            self.return_msg = response['return_msg']
        if 'success' in response:
            self.success = response['success']
