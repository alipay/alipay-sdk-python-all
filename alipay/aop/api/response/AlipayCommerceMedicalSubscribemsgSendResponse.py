#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalSubscribemsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSubscribemsgSendResponse, self).__init__()
        self._error_message = None
        self._msg_id = None
        self._out_msg_id = None
        self._result_code = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSubscribemsgSendResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
        if 'out_msg_id' in response:
            self.out_msg_id = response['out_msg_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
