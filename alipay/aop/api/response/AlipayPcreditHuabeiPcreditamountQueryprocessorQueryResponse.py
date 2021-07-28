#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TbapiQueryAmountResponse import TbapiQueryAmountResponse


class AlipayPcreditHuabeiPcreditamountQueryprocessorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditamountQueryprocessorQueryResponse, self).__init__()
        self._error_context = None
        self._response = None
        self._success = None

    @property
    def error_context(self):
        return self._error_context

    @error_context.setter
    def error_context(self, value):
        self._error_context = value
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, TbapiQueryAmountResponse):
            self._response = value
        else:
            self._response = TbapiQueryAmountResponse.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditamountQueryprocessorQueryResponse, self).parse_response_content(response_content)
        if 'error_context' in response:
            self.error_context = response['error_context']
        if 'response' in response:
            self.response = response['response']
        if 'success' in response:
            self.success = response['success']
