#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationBizfeeAftechSubscribeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationBizfeeAftechSubscribeResponse, self).__init__()
        self._result_code = None
        self._result_message = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationBizfeeAftechSubscribeResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
