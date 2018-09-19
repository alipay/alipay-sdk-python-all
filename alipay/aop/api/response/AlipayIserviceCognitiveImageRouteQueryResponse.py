#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveImageRouteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveImageRouteQueryResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._res = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveImageRouteQueryResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'res' in response:
            self.res = response['res']
        if 'success' in response:
            self.success = response['success']
