#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockMessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockMessageSendResponse, self).__init__()
        self._error_msg = None
        self._trace_id = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockMessageSendResponse, self).parse_response_content(response_content)
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
