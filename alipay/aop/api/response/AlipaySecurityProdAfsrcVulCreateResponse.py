#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdAfsrcVulCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAfsrcVulCreateResponse, self).__init__()
        self._message = None
        self._result = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAfsrcVulCreateResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'result' in response:
            self.result = response['result']
