#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotReceiptSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotReceiptSendResponse, self).__init__()
        self._ext_info = None
        self._receipt_id = None
        self._ret_code = None
        self._ret_code_sub = None
        self._ret_message = None
        self._ret_message_sub = None
        self._success = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self._receipt_id = value
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
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotReceiptSendResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'receipt_id' in response:
            self.receipt_id = response['receipt_id']
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
        if 'ret_code_sub' in response:
            self.ret_code_sub = response['ret_code_sub']
        if 'ret_message' in response:
            self.ret_message = response['ret_message']
        if 'ret_message_sub' in response:
            self.ret_message_sub = response['ret_message_sub']
        if 'success' in response:
            self.success = response['success']
