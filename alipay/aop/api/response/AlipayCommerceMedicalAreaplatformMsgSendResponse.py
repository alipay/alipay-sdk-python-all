#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAreaplatformMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAreaplatformMsgSendResponse, self).__init__()
        self._error_message = None
        self._msg_id_list = None
        self._result_code = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def msg_id_list(self):
        return self._msg_id_list

    @msg_id_list.setter
    def msg_id_list(self, value):
        if isinstance(value, list):
            self._msg_id_list = list()
            for i in value:
                self._msg_id_list.append(i)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAreaplatformMsgSendResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'msg_id_list' in response:
            self.msg_id_list = response['msg_id_list']
        if 'result_code' in response:
            self.result_code = response['result_code']
