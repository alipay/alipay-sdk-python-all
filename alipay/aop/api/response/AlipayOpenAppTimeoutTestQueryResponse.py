#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTimeoutTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTimeoutTestQueryResponse, self).__init__()
        self._timeout = None

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTimeoutTestQueryResponse, self).parse_response_content(response_content)
        if 'timeout' in response:
            self.timeout = response['timeout']
