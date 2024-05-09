#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorIotbspHgnfcSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorIotbspHgnfcSyncResponse, self).__init__()
        self._result = None
        self._ret_code = None
        self._ret_code_sub = None
        self._ret_message = None
        self._ret_message_sub = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def ret_code(self):
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        self._ret_code = value
    @property
    def ret_code_sub(self):
        return self._ret_code_sub

    @ret_code_sub.setter
    def ret_code_sub(self, value):
        self._ret_code_sub = value
    @property
    def ret_message(self):
        return self._ret_message

    @ret_message.setter
    def ret_message(self, value):
        self._ret_message = value
    @property
    def ret_message_sub(self):
        return self._ret_message_sub

    @ret_message_sub.setter
    def ret_message_sub(self, value):
        self._ret_message_sub = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorIotbspHgnfcSyncResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
        if 'ret_code_sub' in response:
            self.ret_code_sub = response['ret_code_sub']
        if 'ret_message' in response:
            self.ret_message = response['ret_message']
        if 'ret_message_sub' in response:
            self.ret_message_sub = response['ret_message_sub']
