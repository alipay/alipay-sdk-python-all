#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPassInstancebatchAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPassInstancebatchAddResponse, self).__init__()
        self._result = None
        self._success = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                self._result.append(i)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserPassInstancebatchAddResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'success' in response:
            self.success = response['success']
