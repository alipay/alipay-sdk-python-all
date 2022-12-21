#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIdeployForcecastCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIdeployForcecastCreateResponse, self).__init__()
        self._op_result = None
        self._op_result_msg = None

    @property
    def op_result(self):
        return self._op_result

    @op_result.setter
    def op_result(self, value):
        self._op_result = value
    @property
    def op_result_msg(self):
        return self._op_result_msg

    @op_result_msg.setter
    def op_result_msg(self, value):
        self._op_result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIdeployForcecastCreateResponse, self).parse_response_content(response_content)
        if 'op_result' in response:
            self.op_result = response['op_result']
        if 'op_result_msg' in response:
            self.op_result_msg = response['op_result_msg']
